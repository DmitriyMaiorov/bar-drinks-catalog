from django.shortcuts import render, get_object_or_404, redirect
from .models import Drink, Category
from .forms import CommentForm

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drink_list.html', {'drinks': drinks})


def drink_detail(request, id):
    drink = get_object_or_404(Drink, id=id)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.drink = drink
        comment.save()
        return redirect('drink_detail', id=id)

    return render(request, 'drinks/drink_detail.html', {
        'drink': drink,
        'form': form
    })


def search(request):
    q = request.GET.get('q', '')
    drinks = Drink.objects.filter(name__icontains=q)
    return render(request, 'drinks/search.html', {'drinks': drinks})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'drinks/categories.html', {'categories': categories})


def like_drink(request, id):
    drink = get_object_or_404(Drink, id=id)
    drink.likes += 1
    drink.save()
    return redirect('drink_detail', id=id)
