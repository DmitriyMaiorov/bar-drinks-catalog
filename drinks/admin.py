from django.contrib import admin
from .models import Drink, Category, Comment, Rating


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume', 'abv', 'likes', 'views')
    list_filter = ('category',)
    search_fields = ('name',)


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
