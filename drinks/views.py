from django.shortcuts import render, get_object_or_404, redirect
from .models import Drink, Category
from django.db.models import Q


def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drink_list.html', {'drinks': drinks})


def drink_detail(request, id):
    drink = get_object_or_404(Drink, id=id)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            drink.comments.create(text=text)
            return redirect('drink_detail', id=id)

    return render(request, 'drinks/drink_detail.html', {'drink': drink})


def like_drink(request, id):
    drink = get_object_or_404(Drink, id=id)
    drink.likes += 1
    drink.save()
    return redirect('drink_detail', id=id)


def search(request):
    q = request.GET.get('q', '')
    drinks = Drink.objects.filter(
        Q(name__icontains=q) |
        Q(ingredients__icontains=q) |
        Q(description__icontains=q)
    )
    return render(request, 'drinks/search.html', {
        'drinks': drinks,
        'query': q
    })



def categories(request):
    categories = Category.objects.all()
    return render(request, 'drinks/categories.html', {'categories': categories})

def drinks_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    drinks = Drink.objects.filter(category=category)
    return render(request, 'drinks/drink_list.html', {
        'drinks': drinks,
        'category': category
    })
