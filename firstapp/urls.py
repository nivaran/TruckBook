from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path("about_us",views.about,name='about'),
    path("contact_us",views.contact,name='contact'),
    path("services",views.services,name='services'),
    path("team",views.team,name='team'),
    path("career",views.career,name='career')
]