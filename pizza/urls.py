from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('komunikat/', views.komunikat, name='komunikat'),
    path('robot/', views.robot, name='robot'),
]