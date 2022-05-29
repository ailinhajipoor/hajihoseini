from django.urls import path
from .views import *

urlpatterns = [
    path('pizza/', pizza, name="pizza"),
    path('ham/', ham, name="ham"),
    path('berenj/', berenj, name="berenj"),
    path('', say_home, name="home"),
]
