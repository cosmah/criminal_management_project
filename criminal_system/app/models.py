# app/models.py
from django.db import models
from django.utils import timezone

class CriminalRecord(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nin = models.CharField(max_length=20)  # Adjust max_length as needed
    crime_committed = models.TextField()
    residence_before_arrest = models.CharField(max_length=255)
    image = models.ImageField(upload_to='criminal_images/')  # Ensure Pillow is installed
    STATUS_CHOICES = [
        ('WANTED', 'Wanted'),
        ('ON_BAIL', 'On Bail'),
        ('SERVING_SENTENCE', 'Serving Sentence'),
        ('COMPLETED_SENTENCE', 'Completed Sentence'),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='WANTED'
    )


    def __str__(self):
        return self.name

class MatchRecord(models.Model):
    criminal_record = models.ForeignKey(CriminalRecord, on_delete=models.CASCADE)
    matched_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255, blank=True, null=True)
    matched_image = models.ImageField(upload_to='matched_images/')

    def __str__(self):
        return f"Match for {self.criminal_record.name} at {self.matched_at}"