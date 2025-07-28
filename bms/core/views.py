from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login


def frontpage(request):
    return render(request, 'components/landing.html')


def about(request):
    return render(request, 'others/about.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = UserRegistrationForm()

    return render(request, 'components/signup.html', {'form': form})
