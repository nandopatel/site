from django import forms

class NameForm(forms.Form):
	#your_name = forms.CharField(label='Name', max_length=100)
	#your_move= forms.CharField(label='Move', max_length=100)
	#yesorno= forms.CharField(label='YesNo', max_length=100)
	distance=forms.CharField(label='Distance Travelled', max_length=100,required=False)
	timetaken=forms.CharField(label='Time taken', max_length=100,required=False)
	mass=forms.CharField(label='Enter mass', max_length=100,required=False)
	gforce=forms.CharField(label='Gravitational force:', max_length=100,required=False)