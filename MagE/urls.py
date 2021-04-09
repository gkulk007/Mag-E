
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = 'Mag-E Dashboard'
admin.site.index_title = 'Welcome to Mag-E Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('clubs/', include("clubs.urls")),
]
