# app/models.py

from django.db import models

class CriminalRecord(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nin = models.CharField(max_length=20)  # Adjust max_length as needed
    crime_committed = models.TextField()
    residence_before_arrest = models.CharField(max_length=255)
    image = models.ImageField(upload_to='criminal_images/')  # Ensure Pillow is installed

    def __str__(self):
        return self.name
