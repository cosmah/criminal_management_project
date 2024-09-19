# app/views.py
import os
from django.conf import settings
from django.shortcuts import render
from .models import CriminalRecord
from .forms import ImageUploadForm
from deepface import DeepFace
import pandas as pd

def citizen_match(request):
    form = ImageUploadForm()
    results = []
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            uploaded_image_path = os.path.join(settings.MEDIA_ROOT, 'temp', uploaded_image.name)
            
            try:
                os.makedirs(os.path.dirname(uploaded_image_path), exist_ok=True)
                
                with open(uploaded_image_path, 'wb+') as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)
                
                print(f"Uploaded image saved at: {uploaded_image_path}")
                
                db_path = os.path.join(settings.MEDIA_ROOT, 'criminal_images')
                print(f"Searching for matches in: {db_path}")
                
                matches = DeepFace.find(img_path=uploaded_image_path, db_path=db_path)
                
                print(f"Matches type: {type(matches)}")
                print(f"Matches content: {matches}")
                
                if isinstance(matches, list) and matches and isinstance(matches[0], pd.DataFrame):
                    df = matches[0]
                    if not df.empty:
                        print("Matches found, processing results")
                        for _, match in df.iterrows():
                            matched_image_path = match['identity']
                            print(f"Matched image path: {matched_image_path}")
                            
                            relative_path = os.path.relpath(matched_image_path, settings.MEDIA_ROOT)
                            relative_path = relative_path.replace(os.path.sep, '/')
                            
                            print(f"Looking for record with image: {relative_path}")
                            
                            record = CriminalRecord.objects.filter(image=relative_path).first()
                            if record:
                                results.append(record)
                                print(f"Record found: {record}")
                            else:
                                print(f"No record found for matched image path: {relative_path}")
                    else:
                        print("DataFrame is empty, no matches found")
                else:
                    print("No matches found by DeepFace or unexpected return format")
            
            except Exception as e:
                print(f"Error during facial recognition: {str(e)}")
                import traceback
                print("Full traceback:")
                print(traceback.format_exc())
            finally:
                if os.path.exists(uploaded_image_path):
                    os.remove(uploaded_image_path)
                    print(f"Uploaded image removed: {uploaded_image_path}")

    return render(request, 'citizen_match.html', {'form': form, 'results': results})


def criminal_record_list(request):
    records = CriminalRecord.objects.all()
    return render(request, 'criminal_record_list.html', {'records': records})

def criminal_record_detail(request, pk):
    record = get_object_or_404(CriminalRecord, pk=pk)
    return render(request, 'criminal_record_detail.html', {'record': record})

def criminal_record_search(request):
    query = request.GET.get('q')
    if query:
        records = CriminalRecord.objects.filter(
            name__icontains=query
        ) | CriminalRecord.objects.filter(
            crime_committed__icontains=query
        ) | CriminalRecord.objects.filter(
            nin__icontains=query
        )
    else:
        records = CriminalRecord.objects.none()  # No results if no query is provided
    
    return render(request, 'criminal_record_search.html', {'records': records, 'query': query})

