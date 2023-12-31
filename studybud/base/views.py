from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm


""" rooms = [
    {"id": 1, "name": "lets learn python!"},
    {"id": 2, "name": "Design with me "},
    {"id": 3, "name": "Frontend developer"},
] """


# rooms in admin.py
def home(request):
    q = request.GET.get('q') if request .GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains = q)
    topics = Topic.objects.all()
    context = {"rooms": rooms,'topics':topics}
    return render(request, "base/home.html", context)


# accessing pk from urls.py  here where we have to display
def room(request, pk):
    room = None
    # connected directly to admin and db
    room = Room.objects.get(id=pk)
    context = {"room": room}

    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
