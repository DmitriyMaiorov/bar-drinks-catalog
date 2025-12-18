from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()

    price = models.IntegerField(default=0)
    volume = models.IntegerField("Объём (мл)", default=0)
    abv = models.FloatField("Крепость %", default=0)

    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings:
            return 0
        return round(sum(r.value for r in ratings) / ratings.count(), 1)

    def __str__(self):
        return self.name


class Rating(models.Model):
    drink = models.ForeignKey(
        Drink,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value} ⭐ для {self.drink.name}'


class Comment(models.Model):
    drink = models.ForeignKey(
        Drink,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий к {self.drink.name}'
