from django.db import models

# Create your models here.

class C1_E(models.Model):
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=200)
	roll=models.IntegerField(default=0)
