from django.urls import path
from . import views

urlpatterns = [
    path('list_event/', views.events, name='list_event'),
    path('request/', views.request, name='request'),
    path('donate/', views.donate, name='donate'),
]