from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password = forms.CharField(widget = forms.PasswordInput())

class AuthorizationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

class Authorization(FormView):
    template_name = "authorization.html"
    form_class = AuthorizationForm
    success_url = '/notes/index/'

    def get_context_data(self, **kwargs):
        context = super(Authorization, self).get_context_data(**kwargs)
        context['auth_form'] = AuthorizationForm()
        context['reg_form'] = RegistrationForm()
        return context


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/notes/index/')
                else:
                    return redirect('/accounts/authorization/', error=True)

        return super(Authorization, self).dispatch(request, *args, **kwargs)

class Register(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if username and (password == confirm_password):
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/notes/index/')

class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            logout(request)