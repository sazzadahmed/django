from django.shortcuts import render
from  django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Teacher
from django.urls import reverse,reverse_lazy
class TeacherListView(ListView):
	template_name='teacher/index.html'
	model=Teacher
	context_object_name='data'

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['flag']='go to bangladesh'
		return  context


class TeacherDetailView(DetailView):
	template_name='teacher/index.html'
	model=Teacher
	context_object_name='data'

class TeacherCreateView(CreateView):
	model=Teacher
	template_name='teacher/create_form_view.html'
	fields='__all__'
	success_url=reverse_lazy('teacher:index1')

class TeacherDeleteView(DeleteView):
	model=Teacher
	template_name='teacher/confirm.html'
	success_url=reverse_lazy('teacher:index1')

		
class TeacherUpdateView(UpdateView):
	model=Teacher
	template_name='teacher/confirm.html'
	fields='__all__'
	success_url=reverse_lazy('teacher:index1')