from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from apps.library.models import Category
from config import settings


class LibraryHomeView(TemplateView):
    template_name = "library/library.html"


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/statistic.html", {

        })


class AllBooksView(View):
    categories = Category.objects.all()
    books = categories[0].books.all()
    # print(books[500].author.all()[0].name)

    def get(self, request):
        return render(request, "library/all-books.html", {
            "categories": self.categories
        })


class MyBooksView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/my-books.html", {

        })


class BorrowedBooksView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/borrowed-books.html", {

        })


class LentBooksView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/lent-books.html", {

        })


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/profile.html", {

        })


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/settings.html", {

        })
