from django.db import models

# Create your models here.
class employee_MS(models.Model):
    name = models.CharField(max_length=200)
    #  = models.IntegerField()
    

