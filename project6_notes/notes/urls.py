from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list_views, name="notes_list")
]
