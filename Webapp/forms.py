from django import forms

from django.forms import ModelForm
from .models import speedandweight
class speednandweightForm(forms.ModelForm):
	class Meta:
		model = speedandweight
		fields = '__all__'
