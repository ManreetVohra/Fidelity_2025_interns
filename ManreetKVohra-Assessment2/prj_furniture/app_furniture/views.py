from app_furniture.serializer import FurnitureSerialization
from app_furniture.models import Furniture
from rest_framework import generics

class CreateFurnitureView(generics.CreateAPIView):
    queryset=Furniture.objects.all()
    serializer_class=FurnitureSerialization

class GetAllFurnitureView(generics.ListAPIView):
    queryset=Furniture.objects.all()
    serializer_class=FurnitureSerialization

class UpdateFurnitureView(generics.UpdateAPIView):
    queryset=Furniture.objects.all()
    serializer_class=FurnitureSerialization
    lookup_field="id"

class DeleteFurnitureView(generics.DestroyAPIView):
    queryset=Furniture.objects.all()
    serializer_class=FurnitureSerialization
    lookup_field="id"
