from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('logindetailspage/',views.logindetails),
    path('home/', views.home),
    path('members/', views.members),
    path('members/details/<int:id>', views.details),
    path('test/', views.testing),
    
]