# app/views.py
import os
import base64
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile
from .models import CriminalRecord, MatchRecord
from .forms import ImageUploadForm
from deepface import DeepFace
import pandas as pd

def citizen_match(request):
    form = ImageUploadForm()
    results = []
    match_found = False  # Flag to indicate if a match was found
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid() or 'image' in request.FILES:
            if 'image' in request.FILES:
                # Handle uploaded file
                image = request.FILES['image']
            else:
                # Handle base64 encoded image from camera
                image_data = base64.b64decode(request.POST['image'].split(',')[1])
                image = ContentFile(image_data, name='captured_image.jpg')

            uploaded_image_path = os.path.join(settings.MEDIA_ROOT, 'temp', image.name)
            
            try:
                os.makedirs(os.path.dirname(uploaded_image_path), exist_ok=True)
                
                with open(uploaded_image_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                
                print(f"Image saved at: {uploaded_image_path}")
                
                db_path = os.path.join(settings.MEDIA_ROOT, 'criminal_images')
                print(f"Searching for matches in: {db_path}")
                
                matches = DeepFace.find(img_path=uploaded_image_path, db_path=db_path)
                
                print(f"Matches type: {type(matches)}")
                print(f"Matches content: {matches}")
                
                if isinstance(matches, list) and matches and isinstance(matches[0], pd.DataFrame):
                    df = matches[0]
                    if not df.empty:
                        print("Matches found, processing results")
                        match_found = True  # Set the flag to True if matches are found
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
                                
                                # Create a MatchRecord
                                match_record = MatchRecord(
                                    criminal_record=record,
                                    location=request.POST.get('location', '')  # You'll need to send this from the frontend
                                )
                                match_record.matched_image.save(
                                    f"match_{record.id}_{match_record.matched_at.strftime('%Y%m%d%H%M%S')}.jpg",
                                    ContentFile(image.read()),
                                    save=True
                                )
                                match_record.save()
                                print(f"Match record created: {match_record}")
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

    return render(request, 'citizen_match.html', {
        'form': form,
        'results': results,
        'match_found': match_found
    })

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