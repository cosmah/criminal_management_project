# app/admin.py

from django.contrib import admin
from .models import CriminalRecord  # Change this line to import CriminalRecord

@admin.register(CriminalRecord)
class CriminalRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nin', 'crime_committed', 'residence_before_arrest')
    search_fields = ('name', 'nin', 'crime_committed')
