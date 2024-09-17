# app/views.py

import os
from django.shortcuts import render, get_object_or_404
from .models import CriminalRecord
from .forms import ImageUploadForm
from deepface import DeepFace
import logging

logger = logging.getLogger(__name__)


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


def citizen_match(request):
    form = ImageUploadForm()
    results = []

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            uploaded_image_path = os.path.join('media', uploaded_image.name)

            try:
                # Save the uploaded image temporarily
                with open(uploaded_image_path, 'wb+') as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)

                # Use DeepFace to find matches in the database images
                matches = DeepFace.find(img_path=uploaded_image_path, db_path='media/criminal_images')  # Adjust path as necessary
                
                # Check if any matches were found
                if matches:
                    for match in matches:
                        matched_image_path = match['identity']  # Get the path of the matched image
                        # Get the corresponding CriminalRecord object based on the matched image path
                        record = CriminalRecord.objects.filter(image=matched_image_path).first()
                        if record:
                            results.append(record)  # Append the full record object

            except Exception as e:
                logger.error(f"Error during facial recognition: {e}")
            finally:
                # Clean up the uploaded file after processing
                if os.path.exists(uploaded_image_path):
                    os.remove(uploaded_image_path)

    return render(request, 'citizen_match.html', {'form': form, 'results': results})