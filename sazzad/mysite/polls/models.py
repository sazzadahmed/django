from django.db import models
from django.urls import reverse,reverse_lazy

class Question(models.Model):
    question_text=models.CharField(max_length=2000)
    pub_date=models.DateTimeField('date of published')
class Choice(models.Model):
    questoin_id=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def get_absolute_url(self):
    	return reverse('polls:listpublisher')


    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
class Sazzad(models.Model):
	name=models.CharField(max_length=100)
	def get_absolute_url(self):
		return reverse('polls:listpublisher')

class SaveMyFirstName(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    fullnam=models.CharField(max_length=30)
