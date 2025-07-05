from django.urls import path
from . import views

urlpatterns = [
    path('myrequest/', views.my_request, name='my_request'),
]