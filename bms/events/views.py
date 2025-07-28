from django.shortcuts import render
from .forms import RequestForm, DonateForm


def events(request):
    return render(request, 'events/list_event.html')


def request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render a success message
    else:
        form = RequestForm()
    return render(request, 'events/request.html', {'form': form})


def donate(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render a success message
    else:
        form = DonateForm()
    return render(request, 'events/donate.html', {'form': form})
