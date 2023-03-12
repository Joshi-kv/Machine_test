from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    role=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    nationality=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    
    def __str__(self):
        return '{}'.format(self.name)