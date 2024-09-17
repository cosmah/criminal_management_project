# app/views.py

from django.shortcuts import render, get_object_or_404  # Import get_object_or_404
from .models import CriminalRecord

def criminal_record_list(request):
    records = CriminalRecord.objects.all()
    return render(request, 'criminal_record_list.html', {'records': records})

def criminal_record_detail(request, pk):
    record = get_object_or_404(CriminalRecord, pk=pk)  # Use the imported function here
    return render(request, 'criminal_record_detail.html', {'record': record})

def criminal_record_search(request):
    query = request.GET.get('q')
    if query:
        # Filter records based on the query
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
