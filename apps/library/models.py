from django.db import models

from apps.core.models import BaseModel
from apps.user.models import User


class Category(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    date_of_birth = models.CharField(max_length=50, null=True)
    works = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=300)
    author = models.ManyToManyField(Author, related_name='books')
    description = models.TextField(null=True)
    year_of_publication = models.CharField(max_length=4)
    publisher = models.CharField(max_length=400, null=True)
    image_url_m = models.URLField(null=True)
    image_url_l = models.URLField(null=True)
    image = models.ImageField(null=True)
    isbn = models.CharField(max_length=50, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='books', null=True)

    def __str__(self):
        return self.title


class Library(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='libraries')

    class Meta:
        verbose_name_plural = 'Libraries'
