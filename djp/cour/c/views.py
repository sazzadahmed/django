from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Te
from .forms import Te_Model_Form
from django.core.urlresolvers import reverse_lazy,reverse
def create_Te(request):
	return render(request,'c/form_create.html',{'form':Te_Model_Form(),})

def create_save_data(request,id=None):
	data=request.POST
	form_data=Te_Model_Form(data)
	#return HttpResponse('<h2>'+ str(id) +'</h2>')



	a=Te()
	a.name=request.POST['name']
	a.address=request.POST['address']
	a.age=request.POST['age']

	if id is not None:
		a.id=id;
	a.save()
	return HttpResponseRedirect(reverse('c:index'))
	



def Te_index(request):
	data=Te.objects.order_by('id')
	return render(request,'c/index.html',{'data':data})
def Te_single(request,id):
	data=Te.objects.filter(id=id)
	return render(request,'c/index.html',{'data':data})
def delete_data(request,id):
	data=Te.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect(reverse('c:index'))
def form_update(request,id):
	data=Te.objects.get(id=id)
	#return HttpResponse('<h2>'+ str(data.name) +'</h2>')
	form_class=Te_Model_Form(initial={'name':data.name,'address':data.address,'age':data.age})
	return render(request,'c/form_update.html',{'id':data.id,'form':form_class})

