from django.urls import path
from apps.library import views

urlpatterns = [
    path('', views.LibraryHomeView.as_view(), name="home")
]
