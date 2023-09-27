from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HandleNotFound(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'core/404.html')
