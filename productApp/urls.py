from django.urls import path

from .views import AddProduct

urlpatterns =[
    path('',AddProduct),
]