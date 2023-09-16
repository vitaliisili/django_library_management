import logging
from functools import reduce

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from apps.library.models import Category, Book, Library

logger = logging.getLogger(__name__)


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


class BookDetailView(View):
    def get(self, request, id):
        logger.info(f"User is authenticated: {request.user.is_authenticated}")
        book = get_object_or_404(Book, id=id)
        library = None

        if request.user.is_authenticated:
            library = Library.objects.get(user=request.user)
            logger.info(f'Library owner: {library.user.username}')

        return render(request, 'library/book-detail.html', {
            'book': book,
            'books': self.get_books(id),
            'library': library
        })

    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        user = request.user

        if not user.is_authenticated:
            return redirect('sign-in')

        library = Library.objects.get(user=user)
        library.books.add(book)
        library.save()
        return redirect('book-detail', id)

    def get_books(self, id):
        book = get_object_or_404(Book, id=id)
        books = Book.objects.filter(
            reduce(lambda x, y: x | y, [Q(title__icontains=word) for word in book.title.split()])).exclude(
            title=book.title)[:10]
        if books.count() < 10:
            logger.warning("Book count are less then 10")
            books_by_category = Book.objects.filter(
                category_id=book.category_id).exclude(id=book.id)[:10 - books.count()]
            return books.union(books_by_category)

        return books


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
