from rest_framework import serializers
from app_quesppr.models import QuestionPaper

class QuestionSerialization(serializers.ModelSerializer):
    class Meta:
        model=QuestionPaper
        fields='__all__'