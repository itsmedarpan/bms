from django.shortcuts import render

def my_request(request):
    return render(request, 'backend/myrequest.html')
