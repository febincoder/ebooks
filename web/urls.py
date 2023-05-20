from django.contrib import admin
from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    
    path('',views.index,name="index"),
    path('register',views.register_1,name="register"),
     path('login',views.login_1,name="login"),

]