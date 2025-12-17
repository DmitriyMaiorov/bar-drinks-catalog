from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    image = models.ImageField(upload_to='drinks/', blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
