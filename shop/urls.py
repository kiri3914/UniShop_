from django.urls import path
from .views import (
    index, about,
    cart, checkout,
    contact, news, shop,
    single_news, single_product)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('shop/', shop, name='shop'),
    path('single_news/', single_news, name='single_news'),
    path('single_product/', single_product, name='single_product'),
]
