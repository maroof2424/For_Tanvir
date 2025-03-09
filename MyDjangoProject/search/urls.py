from django.urls import path
from search.views import search_view

urlpatterns = [
    path('', search_view, name='search'),
]
