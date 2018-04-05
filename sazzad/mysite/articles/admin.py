from django.contrib import admin
from .models import Article
from guardian.admin import GuardedModelAdmin
class ArticleAdmin(GuardedModelAdmin):
	list_display=('title','slug','created_at')
	list_filter=('slug',)
	search_fields=('title',)
admin.site.register(Article,ArticleAdmin)	