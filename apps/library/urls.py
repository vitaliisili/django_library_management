from django.urls import path
from apps.library import views

urlpatterns = [
    path('', views.LibraryHomeView.as_view(), name="home"),
    path('all-books', views.AllBooksView.as_view(), name="all-books"),
    path('book-detail/<int:id>', views.BookDetailView.as_view(), name="book-detail"),
    path('category-books/<int:id>', views.CategoryBookListView.as_view(), name="category-books"),
    path('search-book/<str:search>', views.SearchBookView.as_view(), name='search-book'),
    path('dashboard/statistic', views.DashboardView.as_view(), name="dashboard"),
    path('dashboard/my-books', views.MyBooksView.as_view(), name="my-books"),
    path('dashboard/borrowed-books', views.BorrowedBooksView.as_view(), name="borrowed-books"),
    path('dashboard/lent-books', views.LentBooksView.as_view(), name="lent-books"),
    path('dashboard/profile/<int:pk>', views.ProfileView.as_view(), name="profile"),
    path('dashboard/settings', views.SettingsView.as_view(), name="settings"),
    # path('wishlist', , name="wishlist"),
    # path('become-a-borrower', , name="become-a-borrower"),
]
