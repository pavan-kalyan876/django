from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def india(request):
    return HttpResponse("Karnataka,Andra Pradesh")
