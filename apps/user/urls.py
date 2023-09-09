from django.urls import path
from apps.user import views

urlpatterns = [
    # path('sign-up', views.signup, name='sign-up'),
    path('sign-up', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in', views.SignInView.as_view(), name='sign-in'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('a', views.test, name='a'),
]