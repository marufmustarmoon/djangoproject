from django.db import models

class Value(models.Model):
    date = models.DateField(null=True)
    trade_code = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    openn = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
   
