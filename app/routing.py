from django.urls import path

from .consumers import GameRoom

ws_urlpatterns = [
    path("ws/game/<room_code>/", GameRoom.as_asgi()),
]
