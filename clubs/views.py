from django.shortcuts import render
from .models import Club, Events
# Create your views here.


def clubs_view(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context=context)


def club_detail(request, id):
    club = Club.objects.get(id=id)
    context = {
        'club': club
    }
    return render(request, 'details.html', context=context)
