from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from config import settings


class LibraryHomeView(TemplateView):
    template_name = "library/library.html"


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/statistic.html", {

        })


class AllBooksView(View):
    def get(self, request):
        return render(request, "library/all-books.html", {

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
