from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import C1_E
from django.core.urlresolvers import reverse,reverse_lazy
class C1_E_ListView(ListView):
	model=C1_E
	context_object_name='data'
	template_name='c1/index.html'
class C1_E_CreateView(CreateView):
	model=C1_E
	fields='__all__'
	template_name='c1/create.html'
	success_url=reverse_lazy('c1:index')

class C1_E_View(DetailView):
	model=C1_E
	template_name='c1/detail.html'
	context_object_name='data'
class C1_E_Delete(DeleteView):
	model=C1_E
	template_name='c1/confirm.html'
	success_url=reverse_lazy('c1:index')
class C1_E_Update(UpdateView):
	model=C1_E
	template_name='c1/create.html'
	success_url=reverse_lazy('c1:index')
	fields='__all__'
