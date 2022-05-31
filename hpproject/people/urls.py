from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='people_home'),
    path('name/', views.name_page, name='people_name'),
    path('phone/', views.phone_page, name='people_phone'),
]
