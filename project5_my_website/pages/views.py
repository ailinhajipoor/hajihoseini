from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_page_view(request):
    return render(request, "home.html")


def contact_page_view(request):
    return render(request, "pages/contactus.html")


def about_page_view(request):
    context = {
        'page_name': 'About',
        'description': 'this is  first text',
        'button_value':'dont click',
    }
    return render(request, "pages/about.html",context)
