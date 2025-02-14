from django.urls import path
from .views import *

urlpatterns = [
    path('create/',CreateFurnitureView.as_view()),
    path('getAll/',GetAllFurnitureView.as_view()),
    path('update/<int:id>',UpdateFurnitureView.as_view()),
    path('delete/<int:id>',DeleteFurnitureView.as_view()),
]