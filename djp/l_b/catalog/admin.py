from django.contrib import admin
from .models import Book,Author,BookInstanace,Genre

class BookAdmin(admin.ModelAdmin):
	list_display=['id','title','isbn','author']
admin.site.register(Book,BookAdmin)
class AuthorAdmin(admin.ModelAdmin):
	list_display=['id','first_name','last_name','date_of_birth','date_of_death']
	fields=[('first_name','last_name'),('date_of_birth','date_of_death')]
admin.site.register(Author,AuthorAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display=['id','book']
class GenreAdmin(admin.ModelAdmin):
	list_display=['id','name']

admin.site.register(BookInstanace,BookInstanceAdmin)
admin.site.register(Genre,GenreAdmin)