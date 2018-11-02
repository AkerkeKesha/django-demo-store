from django.shortcuts import render, get_object_or_404
from .models import Product


def show_products(request):
    products = Product.objects.all()
    return render(request, 'shop/product/list.html', {'products': products})


def show_single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product/detail.html', {'product': product})