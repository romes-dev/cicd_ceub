from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Olá Ci/CD, Olá Mundo!")
