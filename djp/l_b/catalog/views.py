from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre,Book,Author,BookInstanace
from django.views.generic import ListView
from django.views.generic.detail import DetailView


def index(request):
	book=Book.objects.filter(title='bangla').count()
	genre=Genre.objects.all().count()
	author=Author.objects.all().count()
	bookinstance=BookInstanace.objects.all().count()
	return render(request,'catelog/local_library_home.html',{
		'book':book,'genre':genre,'author':author,'bookinstance':bookinstance,
		})


class BookListView(ListView):
	model=Book
	context_object_name='data'
	template_name='catelog/list.html'
	paginate_by=1
	def get_queryset(self):
		return Book.objects.all()[:5]
def index1(request,pk):
	return HttpResponse('<h2> This is me </h2>')
class BookDetailView(DetailView):
	model=Book
	template_name='catelog/bookdetail.html'
	context_object_name='book'

	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		context['check']='This is just some data'
		return context
