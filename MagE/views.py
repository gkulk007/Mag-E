from django.shortcuts import render
from clubs import models
from django.utils import timezone


def home(request):

    now = timezone.now()
    event_retrive = models.Events.objects.all()
    upcoming = event_retrive.filter(event_date__gte=now).order_by('event_date')
    for e in upcoming:
        print(e)
    return render(request, "home.html", {'upcoming': upcoming})
