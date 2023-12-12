from django.urls import path
from .views import index, cart, sort_cart

urlpatterns = [
    path('', index, name='index'),
    path('user/<int:user_id>/', cart, name='cart'),
    path('user_sort/<int:user_id>/<int:days_ago>/', sort_cart, name='sort_cart'),
]
