from django.shortcuts import render
from .models import Club, Events
from django.utils import timezone
# Create your views here.


def clubs_view(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context=context)


def club_detail(request, id):
    upcoming = None
    passed = None
    now = timezone.now()
    club = Club.objects.get(id=id)
    event_retrive = Events.objects.all()
    for i in event_retrive:
        if i.event_club.id == id:
            upcoming = event_retrive.filter(
                event_date__gte=now).order_by('event_date')
            passed = event_retrive.filter(
                event_date__lt=now).order_by('-event_date')

    context = {
        'club': club,
        'upcoming': upcoming,
        'passed': passed
    }
    return render(request, 'details.html', context=context)


"""
now = timezone.now()
        upcoming = Event.objects.filter(date__gte=now).order_by('date')
        passed = Event.objects.filter(date__lt=now).order_by('-date')
"""
