from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    drink = models.ForeignKey(
        Drink,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:30]
