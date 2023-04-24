from django.db import models

# Create your models here.

class Tests(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='testimonials/')

    def __str__(self):  # __unicode__ on Python 2
        return self.name
    
    


