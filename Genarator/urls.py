from django.urls import path
from . import views

urlpatterns = [
    path('team', views.team_list, name='team_list'),
]