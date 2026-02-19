from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product
from .services import apply_discount

# Function-based view
def discount_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    apply_discount(product, 10)  # 10% discount
    return redirect("product_list")

# Class-based view
class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
