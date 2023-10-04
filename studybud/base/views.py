
from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    
        {'id':1, 'name':'lets learn python!'},
        {'id':2, 'name':'Design with me '},
        {'id':3, 'name':'Frontend developer'},

    
]
def home(request):
    context = {'rooms':rooms}
    return  render(request,"home.html",context)
def room(request):
    return render(request,'room.html')
