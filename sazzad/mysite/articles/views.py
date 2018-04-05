from django.shortcuts import render
from guardian.compat import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Article
from guardian.mixins import PermissionRequiredMixin, PermissionListMixin
from guardian.shortcuts import assign_perm
class ArticlesCreateView(PermissionListMixin,CreateView):
	model=Article
	template_name='articles/form.html'
	fields='__all__'
	def form_valid(self, *args, **kwargs):
		resp = super(ArticlesCreateView, self).form_valid(*args, **kwargs)
		assign_perm('view_article', self.request.user, self.object)
		assign_perm('change_article', self.request.user, self.object)
		assign_perm('delete_article', self.request.user, self.object)
		return resp

class ArticlesListView(PermissionListMixin,ListView):
	model=Article
	permission_required=['view_article']
class ArticlesDetailView(PermissionRequiredMixin,DetailView):
	model=Article
	permission_required=['view_article']

class ArticleUpdateView(UpdateView):
    model = Article
    permission_required=['view_article','change_article']
    fields = ['title', 'slug', 'content']
class ArticleDeleteView(DeleteView):
    model = Article
    permission_required=['view_article','delete_article']
    success_url = reverse_lazy('articles:list')