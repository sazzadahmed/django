from django.db import models
from guardian.compat import reverse
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
# Create your models here.
class Article(models.Model):
	title=models.CharField('title',max_length=100)
	slug=models.SlugField(max_length=100)
	content=models.TextField('content')
	created_at=models.DateTimeField(auto_now_add=True,db_index=True)

	class Meta:
		permissions=(
			('view_article', 'Can view article'),
			)
		get_latest_by='title'
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('articles:list')
class ArticleUserObjectPermission(UserObjectPermissionBase):
	content_object=models.ForeignKey(Article,on_delete=models.CASCADE)
class ArticleGroupObjectPermission(GroupObjectPermissionBase):
	content_object=models.ForeignKey(Article,on_delete=models.CASCADE)