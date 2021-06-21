from django.shortcuts import render
from clubs import models
from django.utils import timezone


def home(request):

    now = timezone.now()
    event_retrive = models.Events.objects.all()
    upcoming = event_retrive.filter(event_date__gte=now).order_by('event_date')

    return render(request, "home.html", {'upcoming': upcoming})


def eventsPage(request):
    now = timezone.now()
    event_retrive = models.Events.objects.all()
    upcoming = event_retrive.filter(event_date__gte=now).order_by('event_date')
    previous = event_retrive.filter(event_date__lt=now).order_by('event_date')
    context = {
        'upcoming': upcoming,
        'previous': previous}

    return render(request, "events.html", context)
