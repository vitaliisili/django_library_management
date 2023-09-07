from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.user.forms import SignupForm, SigninForm


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
