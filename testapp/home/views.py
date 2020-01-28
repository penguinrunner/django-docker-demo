
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    return HttpResponse('<h1>HELLO WORLDS</h1> <h3>- Penguin</h3>')