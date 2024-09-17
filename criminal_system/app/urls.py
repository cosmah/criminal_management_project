# app/urls.py

from django.urls import path
from .views import book_list, book_search

urlpatterns = [
    path('', book_list, name='book_list'),
    path('search/', book_search, name='book_search'),
]
