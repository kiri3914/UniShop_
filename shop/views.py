from django.shortcuts import render
from .models import \
    Category, Product, CartProduct, Cart, Customer, Order

from django.views.generic import ListView


def index(request):
    products = Product.objects.all()
    return render(request, 'index_2.html', context={'products': products})


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def shop(request):
    return render(request, 'shop.html')


def single_news(request):
    return render(request, 'single-news.html')


def single_product(request):
    return render(request, 'single-product.html')
