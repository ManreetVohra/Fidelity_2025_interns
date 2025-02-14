from rest_framework import serializers
from app_furniture.models import Furniture

class FurnitureSerialization(serializers.ModelSerializer):
    class Meta:
        model=Furniture
        fields='__all__'