from django.shortcuts import render, get_object_or_404
from .models import Drink

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drink_list.html', {'drinks': drinks})

def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drinks/drink_detail.html', {'drink': drink})
