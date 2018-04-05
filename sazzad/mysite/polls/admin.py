from django.contrib import admin
from .models import Question,Choice,Publisher,Book
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Publisher)
admin.site.register(Book)

