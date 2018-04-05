from django.db import models
import uuid
from django.core.urlresolvers import reverse,reverse_lazy
class Genre(models.Model):
	'''
	Models represents a book genre such as science fiction ....
	'''
	name=models.CharField(max_length=200,help_text='general name of genre')

	def __str__(self):
		return self.name

class Book(models.Model):
	title=models.CharField(max_length=200,help_text='Name of the Book')
	author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
	summary=models.TextField(max_length=1000,help_text='over view of the book ')
	isbn=models.CharField('ISBN',max_length=20)
	genre=models.ManyToManyField(Genre,help_text='select the genre of the selected book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('catelog:detail_book',args=[str(self.id)])
	class Meta:
		ordering=['id']
class BookInstanace(models.Model):
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='generate a unique id')
	book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
	inprint=models.CharField(max_length=200)
	due_back=models.DateTimeField(null=True,blank=True)
	loan_status=(('m','Maintenance'),('o','On_loan'),('a','Aviable'),('r','Reserved'))
	stutus=models.CharField(max_length=10,choices=loan_status,blank=True,default='m')

	class Meta:
		ordering=['due_back']
	def __str__(self):
		return '{0} {1}'.format(self.id,self.book.title)
class Author(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	date_of_birth=models.DateTimeField(null=True,blank=True)
	date_of_death=models.DateTimeField('Died',null=True,blank=True)

	def get_absolute_url(self):
		return reverse('detail_authon',args=[str(self.id)])
	class Meta:
		ordering=['last_name','first_name']
	def __str__(self):
		return '{0} {1}'.format(self.first_name,self.last_name)
