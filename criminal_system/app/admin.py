# app/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import CriminalRecord, MatchRecord

@admin.register(CriminalRecord)
class CriminalRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nin', 'crime_committed', 'residence_before_arrest', 'image_tag')
    search_fields = ('name', 'nin', 'crime_committed')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(MatchRecord)
class MatchRecordAdmin(admin.ModelAdmin):
    list_display = ('criminal_record', 'matched_at', 'location', 'matched_image_tag')
    list_filter = ('matched_at',)
    search_fields = ('criminal_record__name', 'criminal_record__nin', 'location')

    def matched_image_tag(self, obj):
        if obj.matched_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.matched_image.url)
        return "-"
    matched_image_tag.short_description = 'Matched Image'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('criminal_record', 'matched_at', 'matched_image')
        return ()