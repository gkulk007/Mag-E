
from django.urls import path
from . import views
urlpatterns = [
    path('', views.clubs_view, name='clubs_view'),
    path('<int:id>/', views.club_detail, name='club_detail'),
]
