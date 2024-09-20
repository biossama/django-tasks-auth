from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def login_user(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('tasks:home')

		else:
			messages.info(request, 'Nom d\'utilisateur ou mot de passe incorrect')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})



def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tasks:home')

	else:
		form = UserCreationForm()
	return render(request, 'accounts/register.html', {'form': form})


def logout_user(request):
     logout(request)
     return redirect('accounts:login-user')
