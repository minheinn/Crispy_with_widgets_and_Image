from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="show_person"),
    path('add-person/', views.AddPerson, name="add_person"),
    path('update-person/<str:pk>/', views.UpdatePerson, name="update_person"),
    path('delete-person/<str:pk>/', views.DeletePerson, name="delete_person"),
    path('view-person/<str:pk>/', views.ViewPerson, name="view_person"),
]
