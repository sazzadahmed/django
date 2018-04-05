from django.db import models


class Teacher(models.Model):
	name=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	age=models.IntegerField(default=30)
	major=models.CharField(max_length=30)
