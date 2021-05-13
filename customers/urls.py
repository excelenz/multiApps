from django.contrib import admin
from django.urls import path

url = [
    path('/admin/customers/customer/<customer:id_customer>/change/', include("api.urls")),
]
