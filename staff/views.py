# global
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

# local
from . import forms


class Register(View):
    def get(self, request):
        registration_form = forms.RegistrationForm()
        context = {
            'registration_form': registration_form
        }
        return render(request, 'staff/registration.html', context=context)

    def post(self, request):
        registration_form = forms.RegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('Login')
        else:
            context = {
                'registration_form': registration_form
            }
            return render(request, 'staff/registration.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'staff/login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('list_services')

        else:
            context = {
                'login_form': login_form
            }
            return render(request, 'staff/login.html', context=context)


class Logout(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('Login')
