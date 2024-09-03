from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm, RegisterUserForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')