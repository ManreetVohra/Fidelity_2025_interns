from django.db import models
from datetime import date

# Create your models here.
class Stock(models.Model):
    sId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    quant=models.IntegerField()
    dop=models.DateField(default=date.today())

    def __str__(self):
        return self.name
