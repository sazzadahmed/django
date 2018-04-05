from django import forms

class Te_Model_Form(forms.Form):
	name=forms.CharField(max_length=200)
	address=forms.CharField(max_length=100)
	age=forms.IntegerField()