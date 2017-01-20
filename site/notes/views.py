from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect

class Notes(TemplateView):
    template_name = "index.html"

    def __init__(self, **kwargs):
        super(Notes, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):

        context = super(Notes, self).get_context_data(**kwargs)
        context['isAuth'] = self.isAuth
        context['user'] = self.user

        return context

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.isAuth = request.user.is_authenticated()
        if self.isAuth:
            return super(Notes, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/accounts/authorization/')