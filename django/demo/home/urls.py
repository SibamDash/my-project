from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),# when we input any url it first comes to home url ==> then to views for the corresponding fn '''

]