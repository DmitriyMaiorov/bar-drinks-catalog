from django.shortcuts import render, get_object_or_404, redirect
from .models import Drink, Category


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
    drinks = Drink.objects.filter(name__icontains=q)
    return render(request, 'drinks/search.html', {'drinks': drinks})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'drinks/categories.html', {'categories': categories})
