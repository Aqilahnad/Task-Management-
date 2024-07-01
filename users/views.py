from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.
def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm
    success_url = reverse_lazy('projects')

def logout_user(request):
   logout(request)
   return redirect("login")

@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def update_profile(request):
   if request.method == 'POST':
       form = ProfileForm(request.POST, instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('tasks')
   else:
       form = ProfileForm(instance=request.user.profile)
  
   context = {'form': form}
   return render(request, 'users/profile_update_form.html', context)