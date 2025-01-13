# contact/urls.py

from django.urls import path
from contact import views

urlpatterns = [
    path("", views.contact, name='contact'),
    path('success/', views.success, name='success')
]