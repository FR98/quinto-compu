from django.db import models

# Create your models here.

class Fruit(models.Model):
	name = models.CharField(max_length = 100)
	color = models.CharField(max_length = 50)

class Vegetable(models.Model):
	name = models.CharField(max_length = 100)
	color = models.CharField(max_length = 50)