from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('scrap/turnover',views.mero_lagani,name="merolagani"),
    path('lagani/home',views.show_mero_lagani,name="merolagani_show"),
]
