from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="show_person"),
    path('add-person/', views.AddPerson, name="add_person"),
]
