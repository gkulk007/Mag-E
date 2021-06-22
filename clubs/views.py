from django.shortcuts import render
from .models import Club, Events, Wanna_Add
from django.utils import timezone
# Create your views here.


def clubs_view(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context=context)


def club_detail(request, id):
    upcoming = []
    passed = []
    now = timezone.now()
    club = Club.objects.get(id=id)
    event_retrive = Events.objects.all()
    for i in event_retrive:
        if i.event_club.id == id:
            # print(i.id)
            # # event_get = Events.objects.get(id=i.event_club.id)
            # print(i)
            if i.event_date >= now:
                upcoming.append(i)
            else:
                passed.append(i)
            # upcoming = event_get.filter(
            #     event_date__gte=now).order_by('event_date')
            # passed = event_get.filter(
            #     event_date__lt=now).order_by('-event_date')

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

        upcoming = event_get.objects.filter(
            event_date__gte=now).order_by('event_date')
        passed = event_get.objects.filter(
            event_date__lt=now).order_by('-event_date')
"""


def wanna_add(request):
    if request.method == 'POST':
        name = request.POST.get('Activity', '')
        club = request.POST.get('Club', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        details = request.POST.get('details', '')

        add = Wanna_Add(activity_title=name, activity_club=club,
                        activity_date=date, activity_time=time, activity_details=details)
        add.save()

    return render(request, 'wanna_add.html')
