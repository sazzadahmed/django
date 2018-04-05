from django.forms import ModelForm,formset_factory
from django import forms
from .models import Question,Publisher,SaveMyFirstName
class CreateQuestionForm(ModelForm):
    class Meta:
        model=Question
        fields='__all__'
        exclude=['pub_date',]
class PublisherFormCreate(ModelForm):
	class Meta:
		model=Publisher
		fields='__all__'
class PlayingWithForm(forms.Form):
	question_text=forms.CharField(max_length=100)
class ContactForm(forms.Form):
	subject=forms.CharField(max_length=100)
	message=forms.CharField(widget=forms.Textarea)
	sender=forms.EmailField()
	cc_myself=forms.BooleanField(required=False)
class QuestionForm(forms.Form):
	name=forms.CharField(max_length=40)
	
class saveMyForm(ModelForm):
	class Meta:
		model=SaveMyFirstName
		fields='__all__'