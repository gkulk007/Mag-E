from django.shortcuts import render
from .models import Club, Events
# Create your views here.


def clubs_view(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context=context)
