from django.db import models

# Create your models here.
class employee_MS(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200) 		#department name or office number
    salary = models.IntegerField()					#salary in thousands
    designation = models.CharField(max_length=200)

    
    
    

