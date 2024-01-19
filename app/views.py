from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

from .models import Game

# Create your views here.


def index(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            option = request.POST["option"]
            room_code = request.POST["room_code"]

            if option == "1":
                game = Game.objects.filter(room_code=room_code).first()

                if game is None:
                    messages.success(request, "Room not found!")
                    return redirect("/")

                if game.is_over:
                    messages.success(request, "Game is over!")
                    return redirect("/")

                game.game_opponent = username
                game.save()
            else:
                game = Game(game_creator=username, room_code=room_code)
                game.save()
            return redirect(f"/play/{room_code}/?username={username}")
        return render(request, "home.html")
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong!")


def play(request, room_code):
    username = request.GET.get("username")
    context = {"room_code": room_code, "username": username}
    return render(request, "play.html", context)
