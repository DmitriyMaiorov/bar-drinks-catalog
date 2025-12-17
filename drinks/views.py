from django.shortcuts import render, get_object_or_404
from .models import Drink

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drink_list.html', {'drinks': drinks})

def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drinks/drink_detail.html', {'drink': drink})

from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'drinks/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    drinks = category.drinks.all()
    return render(request, 'drinks/category_detail.html', {
        'category': category,
        'drinks': drinks
    })
path('categories/', category_list, name='category_list'),
path('categories/<int:category_id>/', category_detail, name='category_detail'),

from django.shortcuts import render
from .models import Drink

def search_drinks(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Drink.objects.filter(name__icontains=query)

    return render(request, "search.html", {"results": results, "query": query})
