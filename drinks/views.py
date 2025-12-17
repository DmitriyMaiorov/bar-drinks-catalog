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

from django.shortcuts import render
from .models import Drink

def search_drinks(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Drink.objects.filter(name__icontains=query)

    return render(request, "search.html", {"results": results, "query": query})

def drink_detail(request, id):
    drink = get_object_or_404(Drink, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.drink = drink
            comment.save()
            return redirect('drink_detail', id=id)
    else:
        form = CommentForm()

    return render(request, 'drink_detail.html', {
        "drink": drink,
        "form": form,
        "comments": drink.comments.all().order_by('-created_at')
    })


from django.shortcuts import render, get_object_or_404
from .models import Drink

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drink_list.html', {'drinks': drinks})

def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drinks/drink_detail.html', {'drink': drink})
