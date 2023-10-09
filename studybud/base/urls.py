from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # if we want to access particularly row,adding dynamic values
    # where <str : pk> it's str = string pk= primary key
    # and pass pk in views
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
]
