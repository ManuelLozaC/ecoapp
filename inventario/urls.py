from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('', views.index),
]
