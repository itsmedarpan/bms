from django.urls import path
from . import views

urlpatterns = [
    path('list_event/', views.events, name='list_event'),
]