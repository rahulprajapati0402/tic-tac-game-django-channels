from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("play/<room_code>/", views.play, name="index"),
]
