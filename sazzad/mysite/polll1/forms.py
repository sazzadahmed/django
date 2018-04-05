from django.forms import ModelForm
from .models import Student,Profile
class StudentsForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'
class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields=__all__