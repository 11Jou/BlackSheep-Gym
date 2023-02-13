from django.urls import path 
from . import views

urlpatterns = [
    path('signup', views.form , name = 'signup'),
    path('login' , views.signin , name='login'),
    path('signout' , views.signout , name='logout'),
]