from django.contrib import admin
from django.urls import path

url = [
    path('/admin/customers/customer/<int:id_customer>/change/', include("api.urls")),
]
