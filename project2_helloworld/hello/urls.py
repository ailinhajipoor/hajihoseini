from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', say_hello, name="hello"),
    path('b/', say_hello, name="hello"),
]
