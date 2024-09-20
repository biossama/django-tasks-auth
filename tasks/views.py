from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TaskForm, CreateUser, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
# Create your views here.


@login_required(login_url='accounts:login-user')
def index(request):
	todos = Todo.objects.filter(user=request.user)
	return render(request, 'tasks/index.html',{'todos':todos})


@login_required(login_url='accounts:login-user')
def add_task(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.user = request.user
			todo.save()
			return redirect('tasks:home')
	form = TaskForm()
	return render(request, 'tasks/add.html', {'form':form})


@login_required(login_url='accounts:login-user')
def update_task(request, pk):
	todo = get_object_or_404(Todo, id=pk, user=request.user)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('tasks:home')
	else:
		form = TaskForm(instance=todo)
	return render(request, 'tasks/update.html', {'form':form})


@login_required(login_url='accounts:login-user')
def remove_task(request, pk):
	todo = get_object_or_404(Todo, id=pk, user=request.user)
	if request.method == 'POST':
		todo.delete()
		return redirect('tasks:home')
	return render(request, 'tasks/delete.html', {'todo':todo})
