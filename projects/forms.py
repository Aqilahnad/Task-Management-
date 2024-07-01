from django.forms import ModelForm
from .models import Task
from django.forms import DateInput
from django.views.generic import ListView

class TaskForm(ModelForm):
  class Meta:
      model =Task
      fields ='__all__'
      widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
               attrs={'type': 'date' }),
               }
      
class TaskListView(ListView):
   model = Task
   template_name = 'projects/tasks.html'
      
