from django.utils import timezone
from django.shortcuts import render
from .models import Category, Product, CartProduct, Cart, Customer, Order

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


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', context={'products': products})


def news(request):
    return render(request, 'news.html')


class ShopView(ListView):
    products = Product.objects.all()
    model = Product
    paginate_by = 15  # if pagination is desired
    template_name = 'index_2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    # return render(request, 'shop.html', context={'products': products})


def single_news(request):
    return render(request, 'single-news.html')


def single_product(request):
    return render(request, 'single-product.html')
