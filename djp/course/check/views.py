from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Check,CheckSub
from .forms import Check as Ch
from django.core.urlresolvers import reverse
def index(request):
	context={
	'data':Check.objects.all().order_by('id')
	}
	template=loader.get_template('check/index.html')

	return HttpResponse(template.render(context,request))

def create(request):
	data=Check()
	data.name=request.POST['name']
	data.address=request.POST['address']
	data.age=request.POST['age']
	data.roll=request.POST['roll']

	data.save()
	return HttpResponseRedirect(reverse('check:index'))
def createform(request):
	template=loader.get_template('check/createform.html')
	return HttpResponse(template.render({},request))
def singleview(request,id):
	context={
	'data':Check.objects.filter(pk=id),
	'singleview':True,
	}
	template=loader.get_template('check/index.html')

	return HttpResponse(template.render(context,request))

def update(request,id):
	context={
	'data':Check.objects.get(pk=id),
	}
	template=loader.get_template('check/updateform.html')
	return HttpResponse(template.render(context,request))

def updateform(request,id):
	data=Check()
	data.id=id;
	data.name=request.POST['name']
	data.address=request.POST['address']
	data.age=request.POST['age']
	data.roll=request.POST['roll']

	data.save()
	return HttpResponseRedirect(reverse('check:index'))
def deletedata(request,id):
	Check.objects.get(pk=id).delete()
	return HttpResponseRedirect(reverse('check:index'))

def single_document_shortcut(request,id):
	data=get_list_or_404(Check,pk=id)
	return render(request,'check/index.html',{'data':data,'singleview':True,})


def createformclass(request):
	form_class=Ch(initial={'name':'sazzad','age':67,})
	
	return render(request,'check/createform.html',{'form':form_class,})


def create_form_data_save(request):
	data=request.POST
	form_class=Ch(data)
	s=""
	if form_class.is_valid():
		q=form_class.clean()
		p=Check()
		p.name=q['name']
		p.address=q['address']
		p.roll=q['roll']
		p.age=q['age']
		p.save()

	return HttpResponseRedirect(reverse('check:index'))

