from django.shortcuts import render
from .models import project
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def proj(request):
	all_project = project.objects.all()
	return render(request, 'project.html', {'all_project': all_project})

class ProjectCreate(CreateView):
	model = project
	template_name = "projform.html"
	fields = ['project_name', 'team_leader','employee']

def details(request,pk):
	detail = project.objects.get(pk=pk)
	return render(request,'details.html',{'detail' : detail})
