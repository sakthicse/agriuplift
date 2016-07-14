from django import forms
from django.forms import ModelForm
from .models import Projects,Query,ProjectQuery

class ProjectsForm(forms.ModelForm):
	name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Project Name'}))
	description = forms.CharField(max_length=100,widget=forms.Textarea)
	image= forms.ImageField()
	class Meta:
		model = Projects
		fields = ['name', 'description','image']

class SearchForm(forms.Form):
	name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Project Name'}))
class QueryForm(forms.ModelForm):
	title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Title'}))
	description = forms.CharField(max_length=100,widget=forms.Textarea)
	class Meta:
		model = Query
		fields = ['title', 'description']


class ProjectQueryForm(forms.ModelForm):
	title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Title'}))
	description = forms.CharField(max_length=100,widget=forms.Textarea)
	class Meta:
		model = Query
		fields = ['title', 'description']
