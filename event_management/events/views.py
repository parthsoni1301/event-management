# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Registration
from django.template import loader
from django.http import HttpResponse

def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        venue = request.POST['venue']
        capacity = request.POST['capacity']
        Event.objects.create(name=name, date=date, venue=venue, capacity=capacity)
        return redirect('events:list')
    return template.render(request, 'create_event.html')

def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Registration.objects.create(event=event, name=name, email=email)
        return redirect('events:detail', event_id=event_id)
    return render(request, 'register_event.html', {'event': event})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    registrations = event.registration_set.all()
    return render(request, 'event_detail.html', {'event': event, 'registrations': registrations})
