from django.urls import path
from . import views
from django.urls import path
from .views import your_view

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
]
