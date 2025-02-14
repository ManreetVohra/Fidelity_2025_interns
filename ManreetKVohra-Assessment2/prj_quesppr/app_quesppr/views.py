from rest_framework.viewsets import ViewSet
from app_quesppr.models import QuestionPaper
from app_quesppr.serializer import QuestionSerialization
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class QuestionViews(ViewSet):
    def list(self,request):
        ques=QuestionPaper.objects.all()
        serialized_ques=QuestionSerialization(ques,many=True)
        return Response(serialized_ques.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        ques=QuestionSerialization(data=request.data)
        if(ques.is_valid()):
            ques.save()
            return Response(ques.data,status=status.HTTP_200_OK)
        return Response(ques.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        temp=pk
        if temp is not None:
            ques=QuestionPaper.objects.get(subcode=temp)
            serialized_ques=QuestionSerialization(ques)
            return Response(serialized_ques.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        temp=pk
        if temp is not None:
            ques=QuestionPaper.objects.get(subcode=temp)
            ques.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        temp=pk
        if temp is not None:
            ques=QuestionPaper.objects.get(subcode=pk)
            serialized_ques=QuestionSerialization(ques,data=request.data)
            if serialized_ques.is_valid():
                serialized_ques.save()
                return Response(serialized_ques.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)