from django.contrib import admin
from django.urls import path
from .views import SnackPageView,DetailPageView,CreateView

urlpatterns = [
    path('',SnackPageView.as_view(), name='snack_list'),
    path('<int:pk>/',DetailPageView.as_view(), name='snack_detail'),
    path('create/',CreateView.as_view(), name= 'snack_create')
]
    
