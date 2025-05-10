from django.urls import path
from . import views

app_name = 'appmuhasebe'

urlpatterns = [
    path("", views.index, name="index"),
    path("defterolur/", views.defterolur, name="defterolur"),
    path('defterolur_delete/<int:id>',views.defterolur_delete_view, name="defterolur_delete_view"), #burda id almamiz gerek
    path('defterolur_edit_view/<int:id>/', views.defterolur_edit_view, name='defterolur_edit_view'),
]