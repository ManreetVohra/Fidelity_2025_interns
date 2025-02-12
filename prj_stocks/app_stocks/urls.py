from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic.edit import CreateView

urlpatterns = [
    path('',Myclass.as_view(),name='home'),
    path('show/',StockList.as_view(),name='show'),
    path('create/',StockCreate.as_view(),name='create'),
    path('update/<int:pk>',StockUpdate.as_view(),name='update'),
    path('delete/<int:pk>',StockDelete.as_view(),name='delete'),
    path('login/',loginPage,name='login'),
    path('register/',registerUser,name='register')
]