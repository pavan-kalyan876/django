from django.db import models
from django.db.models import Model
# Create your models here.

class Room(models.Model):
    # host
    # topic
      name = models.name = models.CharField(max_length=250)
      description = models.TextField(blank=True, null=True)
    #participants = models

      updated = models.DateTimeField(auto_now=True)

    #create datetime fields in the database that are automatically updated to the current datetime.
      created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
        return self.name
    