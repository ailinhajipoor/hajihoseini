from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ham(request):
    return HttpResponse("hamburger")


def pizza(request):
    return HttpResponse("pizza")


def berenj(request):
    return HttpResponse("berenj")
def say_home(request):
    return HttpResponse("<html><head><head><body><pre>/ \</pre><pre>| |</p><pre>| |</pre></body></html>")

