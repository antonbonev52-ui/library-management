from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published_date = models.DateField()

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
