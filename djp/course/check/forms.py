from django import forms

class Check(forms.Form):
	name=forms.CharField(max_length=200)
	address=forms.CharField(max_length=200)
	roll=forms.CharField(max_length=200)
	age=forms.IntegerField()

