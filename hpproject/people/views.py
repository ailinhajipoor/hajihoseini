from django.shortcuts import render
from .models import Person
from django.http import HttpResponse


def home_page(request):
    data = Person.objects.all()
    return render(request, "people/home_page.html", {"data": data})


def name_page(request):
    data = Person.objects.all()
    return render(request, "people/name_page.html",{"data": data})


def phone_page(request):
    data = Person.objects.all()
    return render(request, "people/phone_page.html",{"data": data})
