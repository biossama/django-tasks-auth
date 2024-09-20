from .models import Todo
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



# register
class CreateUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']


# login
class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())


# create form
class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"add new Task"}))
	class Meta:
		model = Todo
		fields = "__all__"
		exclude = ('user',)
