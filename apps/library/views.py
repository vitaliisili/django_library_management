from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class LibraryHomeView(TemplateView):
    template_name = "library/library.html"


class DashboardView(View):
    def get(self, request):
        return render(request, "library/dashboard.html", {

        })

class AllBooksView(View):
    def get(self, request):
        return render(request, "library/all-books.html", {

        })