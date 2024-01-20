from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login/', views.login),
    path('members/', views.members),
    path('members/details/<int:id>', views.details),
    path('test/', views.testing),
    path('login/logindetailspage/',views.logindetails)
    
]