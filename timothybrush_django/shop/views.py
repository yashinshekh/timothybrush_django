from django.shortcuts import render,HttpResponse
from .models import Product


def shop(request):
    products = Product.objects.all()
    if products:
        return render(request, 'shop/home.html', {'products': products})
    else:
        return HttpResponse('<h1>No product available</h1>')
