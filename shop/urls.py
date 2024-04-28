from django.contrib import admin
from django.urls import path
from .views import index, product_detail

urlpatterns = [
    path('', index),
    path('product/<int:pk>', product_detail)
]