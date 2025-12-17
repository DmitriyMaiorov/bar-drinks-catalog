from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='drinks/', blank=True)

    def __str__(self):
        return self.name
