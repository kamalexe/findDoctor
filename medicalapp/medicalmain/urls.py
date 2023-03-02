from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment-registration', views.appointmentView, name='appointmentView'),
    path('appointment-registration/appointment', views.appointment, name='appointment'),
    path('track-appointment', views.trackappointment, name='trackappointment'),
    path('track', views.track, name='track'),
    path('price', views.priceView, name='priceView'),
    path('about', views.aboutView, name='aboutView'),
    path('service', views.serviceView, name='serviceView'),
    path('btnappoint', views.btnappoint, name='btnappoint'),
    path('find-doctor', views.findDoct, name='findDoct'),
    path('doctProfile/<slug:slug>', views.doctProfileView, name='doctProfileView'),
    path('contact', views.contactDoct, name='contactDoct'),
    path('contactForm', views.contactForm, name='contactForm'),
    path('reviewForm', views.reviewForm, name='reviewForm'),


]
