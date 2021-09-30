from django.urls import path
from app_two.views import index

urlpatterns =[
    path('', index),
]