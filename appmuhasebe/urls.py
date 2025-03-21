from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("defterolur/", views.defterolur, name="defterolur"),
]