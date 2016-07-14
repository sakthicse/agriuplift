""" Views for the base application """

from django.shortcuts import render
from .forms import ProjectsForm,QueryForm,SearchForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Projects,ProjectQuery

def home(request):
    """ Default view for the root """

    return render(request, 'base/home.html')

class ProjectView(TemplateView):
	template_name = 'base/view-project.html'    
	def get(self,request,project_id):
		try:
			projects = Projects.objects.filter(pk=project_id)
			
		except Exception, e:
			projects = []
			
		try:
			query = ProjectQuery.objects.filter(project=project_id)
		except:
			query = []
		
		return render(request, self.template_name, {"projects": projects,"querys":query})

	

class ProjectAddView(TemplateView):
	template_name = 'base/add-project.html'    
	def get(self,request):
		form = ProjectsForm
		return render(request, self.template_name, {"form": form})

	def post(self,request):

		#template_name = 'add-project.html'
		data = request.POST
		form = ProjectsForm(request.POST,request.FILES)
		if form.is_valid():
			project=form.save(commit=False)
			project.created_by=request.user
			project.save()
			#return HttpResponseRedirect('/')
			return render(request, 'base/home.html', {"success_message": "success"})
		return render(request, self.template_name, {"form": form})
	
class QueryView(TemplateView):
	pass
class QueryAddView(TemplateView):
	template_name = 'base/add-query.html'    
	def get(self,request):
		form = QueryForm
		return render(request, self.template_name, {"form": form})
	def post(self,request):
		data = request.POST
		form = QueryForm(request.POST)
		if form.is_valid():
			query=form.save(commit=False)
			query.created_by=request.user
			query.save()
			#return HttpResponseRedirect('/')
			return render(request, 'base/home.html', {"success_message": "success"})

class ProjectQueryAddView(TemplateView):
	template_name = 'base/project-add-query.html'    
	def get(self,request,project_id):
		form = ProjectQueryForm
		return render(request, self.template_name, {"form": form,"project_id":project_id})
	def post(self,request):
		data = request.POST
		form = ProjectQueryForm(request.POST)
		if form.is_valid():
			query=form.save(commit=False)
			query.created_by=request.user
			query.project_id=data['project_id']
			query.save()
			#return HttpResponseRedirect('/')
			return render(request, 'base/home.html', {"success_message": "success"})

class ProjectSearchView(TemplateView):
	template_name = 'base/home.html'    
	def get(self,request):
		data = request.GET
		name=data.get('name')
		form = SearchForm(data)
		projects = Projects.objects.filter(name=name,is_apprival=True)

		return render(request, self.template_name, {"projects": projects,"form":form})

	

	def post(self,request):
		pass

		# template_name = 'base/home.html'
		# data = request.POST
		# name=data['name']
		# projects = Projects.objects.filter(name=name,is_apprival=True)
		
		# return render(request, template_name, {"projects": projects})



		

