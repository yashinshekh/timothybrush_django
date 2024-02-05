from django.shortcuts import render,HttpResponse
from .models import Product


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

