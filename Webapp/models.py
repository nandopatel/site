from django.db import models

# Create your models here.
class speedandweight(models.Model):
	comments=models.IntegerField(blank=True)
	weight=models.IntegerField(blank=True)
	Gravitational_Force=models.CharField(max_length=350,blank=True)
	mass=models.CharField(max_length=350,blank=True)
	time=models.CharField(max_length=350,blank=True)
	distance_travelled=models.CharField(max_length=350,unique=True)
	speed=models.CharField(max_length=350,blank=True)
	