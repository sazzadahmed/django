from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.forms import formset_factory,modelformset_factory
from django.urls import reverse_lazy,reverse
from .models import Question,Choice,Publisher,Book,Sazzad,Author,SaveMyFirstName
from .forms import CreateQuestionForm,PublisherFormCreate,ContactForm,PlayingWithForm,QuestionForm,saveMyForm
from django.utils import timezone
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,FormView,DeleteView,FormView
def index(request):
    data=Question.objects.all()
    template=loader.get_template('polls/index.html')
    return HttpResponse(template.render({'data':data},request))
def create(request):
    if request.method=='POST':
        a=CreateQuestionForm(request.POST)
        b=a.save(commit=False)
        b.pub_date=timezone.now()
        data = Question.objects.all()
        b.save()
    else:
        a=CreateQuestionForm()
        template=loader.get_template('polls/createform.html')
        return HttpResponse(template.render({'a':a, },request))
    return render(request,'polls/index.html',{'data':data})
def view(request,pk):
    a=Question.objects.get(pk=pk)
    context={'singledata':a}
    return render(request,'polls/index.html',context)
def update(request,pk):
    if request.method=='POST':
        a=CreateQuestionForm(request.POST)
        b=a.save(commit=False)
        b.pub_date=timezone.now()
        b.id=pk
        b.save()
        data = Question.objects.all()

        return render(request, 'polls/index.html', {'data': data})

    else:
        #using the existing create form
        data=Question.objects.get(pk=pk)
        return render(request,'polls/edit.html',{'data':data})
def delete(request,pk):
    a=Question.objects.filter(pk=pk)
    a.delete()
    data=Question.objects.all()
    return render(request, 'polls/index.html', {'data': data})

class QuestionListView(CreateView):
    model = Question
    context_object_name = 'fineform'
    template_name = 'polls/createview.html'
    fields = ['question_text',]


class EditQuestionView(UpdateView):
    model = Question
    fields = ['question_text',]
    template_name ='polls/updateview.html'
    context_object_name = 'update'
    success_url = reverse_lazy('polls:index')
class QuestinDetailView(DetailView):
    model = Question
    context_object_name = 'singledata'
    template_name = 'polls/index.html'
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/delete.html'
    context_object_name = 'delete'
    success_url='../'
class PublisherCreateView(CreateView):
    model=Publisher
    fields='__all__'
    template_name='polls/publish.html'
class PublisherUpdateView(UpdateView):
    model=Publisher
    fields='__all__'
    template_name='polls/publish.html'

class PublisherDeleteView(DeleteView):
    model=Publisher
    context_object_name='form'
    success_url=reverse_lazy('polls:listpublisher')
class PublishListView(ListView):
    model=Publisher
    template_name='polls/pushlish_list.html'
    context_object_name='publisher'

class SazzadSpecialCheck(FormView):
    '''This class is build for testing the form_valid mehtod
    and its functionality'''
    template_name='polls/check.html'
    form_class=PublisherFormCreate
    success_url=reverse_lazy('polls:listpublisher')
    def form_valid(self,form):
        form.save()
        return super(SazzadSpecialCheck,self).form_valid(form)

class Contant(FormView):
    template_name='polls/contactform.html'
    form_class=ContactForm
    context_object_name="formal"
def UseSameFormForCreateAndUpdate(request,id):
    '''this was created for checking something'''
    pass
def functiontest(request):
    if request.method=='POST':
        a=Question()
        a.question_text=request.POST['question_text']
        a.pub_date=timezone.now()
        a.save()
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        a=PlayingWithForm()
        return render(request,'polls/test.html',{'form':a})
def formsettest(request):
    a=formset_factory(CreateQuestionForm,extra=8,max_num=10)
    b=a(initial=[{'question_text':'what is your nnnnname?? ',}])
    return render(request,'polls/formset.html',{'context':b,})

def QuestionFormView(request):
    multiquestionform=modelform_factory(Author,fields=['salutation','name','email'])
    if request.method=='POST':
        instances=multiquestionform(request.POST,request.FILES)
        
        if instances.is_valid():
            instances.save()
            return HttpResponseRedirect(reverse('polls:index'))


    objectform=multiquestionform()

    return render(request,'polls/test.html',{'form':objectform})
def saveMyspecialFuction(request):
    ob=modelformset_factory(SaveMyFirstName,fields='__all__',extra=3,max_num=5)
    if request.method=='POST':
        objct=ob(request.POST,request.FILES)
        objects=objct.save(commit=False)
        s=' this is  mr khan '
        for a in objects:
            a.save()


        return HttpResponse('<h2>'+s+'</h2>')
    else:
        objectform=ob()
        return render(request,'polls/test.html',{'form':objectform})

