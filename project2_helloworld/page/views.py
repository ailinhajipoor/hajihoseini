from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_something(request):
    return HttpResponse(">\(o_O)/<")