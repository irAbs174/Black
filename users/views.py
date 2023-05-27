'''
Accounts views :
'''

#Import all requirements
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from allauth.account.views import LoginView
from .forms import CustomUserCreationForm, CustomUserChangeForm, LoginForm
from .models import CustomUser


class Register(View):
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = self.request.POST['username']
            password = self.request.POST['password1']
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect('dashboard')
        else:
            context = {'form': form}
            return render(request, 'accounts/register.html', context)

    def get(self, request):
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm