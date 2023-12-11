from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    



class Capital(models.Model):
    name=models.ForeignKey(Country,on_delete=models.CASCADE)
    place=models.CharField(max_length=100)

    
