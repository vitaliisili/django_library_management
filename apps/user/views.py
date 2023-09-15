from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.library.models import Book, Category, Author
from apps.user.forms import SignupForm, SigninForm
from config import settings


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'user/sign-up.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class SignInView(LoginView):
    login = 'sign-in'
    template_name = 'user/sign-in.html'
    authentication_form = SigninForm


class UserLogoutView(LogoutView):
    logout = 'logout'


def test(request):
    import requests
    books = Book.objects.filter(description__isnull=True)

    for book in books:
        title = book.title.replace(' ', '%')
        try:
            req = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={title}&maxResults=1')
            data = req.json()
            description = data['items'][0]['volumeInfo']['description']

            current_book = Book.objects.get(pk=book.id)
            current_book.description = description
            current_book.save()
            print("DONE: ", book.id)
        except Exception as err:
            pass
            print('ERROR:', err)
            print("NOT FOUND DESCRIPTION: ", book.id)


    return render(request, 'user/test.html', {

    })
