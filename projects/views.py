from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def current_time(request):
   current_date_time = datetime.datetime.now()
   return HttpResponse(f"The Current time: {current_date_time}")

def home(request):
    return render(request, 'index.html')
 
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{'projects': projects})

@login_required()
def projectList(request):
   projects = Project.objects.all()
  
   context = {'projects':projects}
   return render(request, 'projects/projects.html',context)

@login_required
def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'projects/project-detail.html',context)

@login_required
def taskList(request):
    user_tasks =Task.objects.filter(assignee=request.user) #fetches all the tasks assigned to the currently logged-in user and other unassigned tasks
    tasks = Task.objects.filter(assignee=None) #fetches all unassigned tasks
 
    context = {'tasks':tasks,'user_tasks':user_tasks}
    return render(request, 'projects/tasks.html',context)

@login_required
def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk) #retrieve the task object or raise a 404 error if the task object doesn’t exist
    context = {'task':task}
    return render(request, 'projects/task-detail.html',context)

@login_required
def taskCreate(request):
   form = TaskForm
   if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
           form.save()   
           return redirect('tasks')
   context = {'form':form}
   return render(request, 'projects/task-create.html',context)

class ProjectCreateView(CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update_form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'projects/task_update_form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'
    success_url = reverse_lazy('projects')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('tasks')

@login_required
def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')

def dashboard_view(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects': projects,
        'tasks': tasks,
    }
    return render(request, 'projects/dashboard.html', context)