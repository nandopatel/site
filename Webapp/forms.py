from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='Name', max_length=100)
	your_move= forms.CharField(label='Move', max_length=100)
	yesorno= forms.CharField(label='YesNo', max_length=100)