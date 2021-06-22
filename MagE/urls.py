
from django.contrib import admin
from django.urls import path, include
from . import views
from clubs import views as vs

admin.site.site_header = 'Mag-E Dashboard'
admin.site.index_title = 'Welcome to Mag-E Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('events/', views.eventsPage, name='event_page'),
    path('devs/', views.developersPage, name='dev_page'),
    path('clubs/', include("clubs.urls")),
    path('wanna-add/', vs.wanna_add, name='wanna_add'),
]
