from django.urls import path
from .views import *

urlpatterns = [
    path('test/', say_bye, name="bye"),
]
