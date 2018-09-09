from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.show_products, name = 'product_list'),
    path('<int:product_id>', views.show_single_product, name='product_detail'),
]