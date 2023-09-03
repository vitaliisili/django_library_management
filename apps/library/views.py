from django.shortcuts import render
from django.views import View


class LibraryHomeView(View):
    def get(self, request):
        return render(request, "library/library.html", {
            "test": "Library Home Page"
        })
