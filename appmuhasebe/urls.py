from django.urls import path
from . import views

app_name = 'appmuhasebe'

urlpatterns = [
    path("", views.index, name="index"),
    path("defterolur/", views.defterolur, name="defterolur"),
]