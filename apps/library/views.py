from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from apps.library.models import Category, Book
from config import settings


class LibraryHomeView(TemplateView):
    template_name = "library/library.html"


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "library/statistic.html", {

        })


class AllBooksView(ListView):
    model = Category
    template_name = 'library/all-books.html'
    context_object_name = 'categories'


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book-detail.html'
    context_object_name = 'book'

    def get_books(self):
        books = Book.objects.filter(
            reduce(lambda x, y: x | y,
                   [Q(title__icontains=word) for word in self.object.title.split()]))[:10]
        if books.count < 10:
            books_by_category = Book.objects.filter(category_id=self.object.id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(
            reduce(lambda x, y: x | y,
                   [Q(title__icontains=word) for word in self.object.title.split()]))[:10]
        return context


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
