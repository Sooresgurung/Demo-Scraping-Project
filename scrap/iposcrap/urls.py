from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ipo/scrap/',views.ipo_fetch,name="ipofetch"),
    path('ipo/home/',views.show_upcoming_ipo,name="upcoming_ipo"),
]
