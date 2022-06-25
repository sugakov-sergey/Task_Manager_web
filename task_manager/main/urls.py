from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('about/', views.about, name='about'),
    path('purpose/', views.purpose, name='purpose'),
]
