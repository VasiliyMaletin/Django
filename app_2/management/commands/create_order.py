from django.core.management.base import BaseCommand
from app_2.models import User, Order, Product


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('User_id', type=int, help='User ID')
        parser.add_argument('-p', '--Product_id', nargs='+', help='User ID', required=True)

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('User ID')
        product_id: list = kwargs.get('Product ID')
        user = User.objects.filter(pk=user_id).first()
        order = Order(customer=user)
        total_price = 0
        for i in range(0, len(product_id)):
            product = Product.objects.filter(pk=product_id[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.products.add(product)
