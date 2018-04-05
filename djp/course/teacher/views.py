from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Teacher
from django.core.urlresolvers import reverse

def index(request):
	template=loader.get_template('teacher/index.html')
	context={
	'data':Teacher.objects.all()
	}
	return HttpResponse(template.render(context,request))
	
def create(request):
	template=loader.get_template('teacher/form.html')
	return HttpResponse(template.render({},request))
def formdata(request):

	data=Teacher()
	data.name=request.POST['name']
	data.title=request.POST['title']

	data.major=request.POST['major']

	data.save()
	return HttpResponseRedirect(reverse('teacher:index'))

def single_view(request,id):
	data=Teacher.objects.filter(pk=id)
	context={
	'data':data
	}
	template=loader.get_template('teacher/index.html')
	return HttpResponse(template.render(context,request))

def update(request,id):
	data=Teacher.objects.get(pk=id)
	context={
	'form':data
	}
	template=loader.get_template('teacher/form.html')
	return HttpResponse(template.render(context,request))
def formdata_update(request,id):
	a=Teacher()
	a.id=id
	a.name=request.POST['name']
	a.title=request.POST['title']
	a.major=request.POST['major']
	a.save();
	return HttpResponseRedirect(reverse('teacher:index'))

def delete_data(request,id):
	a=Teacher.objects.get(pk=id)
	a.delete()
	return HttpResponseRedirect(reverse('teacher:index'))
