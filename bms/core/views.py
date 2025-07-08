from django.shortcuts import render


def frontpage(request):
    return render(request, 'components/landing.html')

def about(request):
    return render(request, 'others/about.html')