from django.urls import path
from apps.library import views

urlpatterns = [
    path('', views.LibraryHomeView.as_view(), name="home"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard"),
    path('all-books', views.AllBooksView.as_view(), name="all-books"),
]
