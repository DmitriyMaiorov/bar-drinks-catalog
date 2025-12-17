from django.contrib import admin
from .models import Drink, Category, Comment, Rating

admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
