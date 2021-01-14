from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

class Title(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

class GenreTitle(models.Model):
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
