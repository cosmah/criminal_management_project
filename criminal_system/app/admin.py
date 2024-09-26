# app/admin.py
from django.contrib import admin
from .models import CriminalRecord, MatchRecord

@admin.register(CriminalRecord)
class CriminalRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nin', 'crime_committed', 'residence_before_arrest')
    search_fields = ('name', 'nin', 'crime_committed')

@admin.register(MatchRecord)
class MatchRecordAdmin(admin.ModelAdmin):
    list_display = ('criminal_record', 'matched_at', 'location')
    list_filter = ('matched_at',)
    search_fields = ('criminal_record__name', 'criminal_record__nin', 'location')
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('criminal_record', 'matched_at', 'matched_image')
        return ()