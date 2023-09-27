from django.contrib import admin
from django.urls import path, include

from apps.core.views import HandleNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.library.urls")),
    path('auth/', include("apps.user.urls")),
]

handler404 = HandleNotFound.as_view()
