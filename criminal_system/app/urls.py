# app/urls.py

from django.urls import path
from .views import criminal_record_detail, criminal_record_search, citizen_match, criminal_record_list

urlpatterns = [
    # Match URL for citizen_match view
    path('', citizen_match, name='citizen_match'),
    
    # Match URL for criminal record detail view
    path('record/<int:pk>/', criminal_record_detail, name='criminal_record_detail'),
    
    # Match URL for search functionality
    path('search/', criminal_record_search, name='criminal_record_search'),

    path('criminal-records/', criminal_record_list, name='criminal_record_list'),
]
