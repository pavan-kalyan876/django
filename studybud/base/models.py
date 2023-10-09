from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # connected to topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    # participants = models

    updated = models.DateTimeField(auto_now=True)

    # create datetime fields in the database that are automatically updated to the current datetime.
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# cascade means
# each room has a message creating a room
# one to many relation ship
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # connecting to room by foreign key
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.body
