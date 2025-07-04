from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('sorteio.urls')),
]

