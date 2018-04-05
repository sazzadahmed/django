from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=100)
	add=models.CharField(max_length=200)
class Profile(models.Model):
	sure_name=models.CharField(max_length=100)
	student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
