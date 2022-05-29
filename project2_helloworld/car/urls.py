from django.urls import path
from .views import *

urlpatterns = [
    path('lam/', lam, name="lam"),
    path('pride/', pride, name="pride"),
    path('', say_home, name="home"),

]
