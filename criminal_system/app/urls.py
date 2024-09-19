# app/urls.py

from django.urls import path
from .views import criminal_record_list, criminal_record_detail, criminal_record_search, citizen_match

urlpatterns = [
    path('', criminal_record_list, name='criminal_record_list'),
    path('record/<int:pk>/', criminal_record_detail, name='criminal_record_detail'),
    path('search/', criminal_record_search, name='criminal_record_search'),
    path('match/', citizen_match, name='citizen_match'),  # Ensure this line is present
]
