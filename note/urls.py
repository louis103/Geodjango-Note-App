from django.urls import path, include
from . import views


urlpatterns = [
    path("map/", views.index, name="index"),
    path("note/", views.note, name="note"),
]
