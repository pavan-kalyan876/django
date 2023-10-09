from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


""" rooms = [
    {"id": 1, "name": "lets learn python!"},
    {"id": 2, "name": "Design with me "},
    {"id": 3, "name": "Frontend developer"},
] """


# rooms in admin.py
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


# accessing pk from urls.py  here where we have to display
def room(request, pk):
    room = None
    # connected directly to admin and db
    room = Room.objects.get(id=pk)
    context = {"room": room}

    return render(request, "base/room.html", context)


def createRoom(request):
    context = {}
    return render(request, "base/room_form.html", context)
