from django.shortcuts import render
from .models import project
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def proj(request):
	all_project = project.objects.all()
	return render(request, 'project.html', {'all_project': all_project})

class ProjectCreate(CreateView):
	model = project
	fields = ['project_name','employee','start_date','end_date']

def details(request,pk):
	detail = project.objects.get(pk=pk)
	return render(request,'details.html',{'detail' : detail})
