from django.contrib import admin
from django.urls import path, include
from outputDB import views

urlpatterns = [
    path('getStudent', views.queryGetStudent)
]