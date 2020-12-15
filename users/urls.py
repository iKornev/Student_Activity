"""Определяет схемы URL для пользователей"""

from django.contrib.auth.views import  LoginView, LogoutView 
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views



app_name = "users"
urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),

    #url(r'^logout/$', views.logout_view, name='logout'),

    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
   
]