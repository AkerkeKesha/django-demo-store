from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products_list'


class ProductDetail(DetailView):
    template_name = 'shop/product/detail.html'
    model = Product

