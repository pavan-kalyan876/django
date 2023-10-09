from django.forms import ModelForm
from .models import Room


# writing for the Room imported from the models
#meta is used to control the behavior of model in variety of ways,such changing the table name,
#or custom validation rules
# fields =__all__ ,we are using that what are the fields are there in ROOM in model every fields will be accessing or 
#everything here
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
