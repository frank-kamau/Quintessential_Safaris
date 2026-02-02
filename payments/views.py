from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def payment_home(request):
    return HttpResponse("Payments app is working!")

