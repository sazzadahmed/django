from django.db import models


class Check(models.Model):
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	roll=models.CharField(max_length=200)
	age=models.IntegerField(default=50)
	
		
class CheckSub(models.Model):
	check_id=models.ForeignKey(Check,on_delete=models.CASCADE)
	name=models.CharField(max_length=300)