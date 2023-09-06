from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class LibraryHomeView(TemplateView):
    template_name = "library/library.html"


class DashboardView(View):
    def get(self, request):
        return render(request, "library/statistic.html", {

        })


class AllBooksView(View):
    def get(self, request):
        return render(request, "library/all-books.html", {

        })


class MyBooksView(View):
    def get(self, request):
        return render(request, "library/my-books.html", {

        })


class BorrowedBooksView(View):
    def get(self, request):
        return render(request, "library/borrowed-books.html", {

        })


class LentBooksView(View):
    def get(self, request):
        return render(request, "library/lent-books.html", {

        })


class ProfileView(View):
    def get(self, request):
        return render(request, "library/profile.html", {

        })


class SettingsView(View):
    def get(self, request):
        return render(request, "library/settings.html", {

        })