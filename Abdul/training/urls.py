from django.contrib import admin
from django.urls import path
from .views import home , contact, about, services
from training import views

urlpatterns = [
    path('',views.home, name = 'home' ),
    path('contact',views.contact, name = 'contact'),
    path('about',views.about, name = 'about'),
    path('services', views.services, name = 'services'),


]
