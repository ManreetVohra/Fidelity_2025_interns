from django.db import models
from datetime import date
# Create your models here.

class Furniture(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    quant=models.IntegerField()
    dop=models.DateField(default=date.today())

    def __str__(self):
        return self.name
