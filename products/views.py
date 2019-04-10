from django.shortcuts import render
from .models import Product

from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class ProductList(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

