from django.db import models

# Create your models here.
class speedandweight(models.Model):
	comments=models.IntegerField(blank=True)
	weight=models.IntegerField(blank=True)
	Gravitational_Force=models.FloatField(max_length=350,blank=True)
	mass=models.IntegerField(max_length=350,blank=True)
	time=models.IntegerField(max_length=350,blank=True)
	distance_travelled=models.IntegerField(max_length=350,unique=True)
	speed=models.IntegerField(max_length=350,blank=True)


class pivx(models.Model):
	price=models.FloatField()
	percent_change=models.FloatField()
