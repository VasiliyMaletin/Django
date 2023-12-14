from django.shortcuts import render
from datetime import datetime, timedelta
from .models import User, Order


def index(request):
    return render(request, 'app_3/index.html')


def cart(request, user_id: int):
    products = {}
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    for order in orders:
        products[order] = order.products.all()
    print(products)
    return render(request, 'app_3/all_orders.html', {'user': user, 'products': products})


def sort_cart(request, user_id: int, days_ago: int):
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered_range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)
    return render(request, 'app_3/all_product.html', {'user': user, 'product_set': product_set, 'days': days_ago})
