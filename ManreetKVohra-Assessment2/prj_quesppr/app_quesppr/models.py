from django.db import models

# Create your models here.
class QuestionPaper(models.Model):
    subcode=models.IntegerField(primary_key=True)
    qno=models.IntegerField()
    subject=models.CharField(max_length=50)
    question=models.IntegerField()
    
    def __str__(self):
        return  self.subject
