from django.core.management.base import BaseCommand
from app_2.models import User


class Command(BaseCommand):
    help = 'Create User'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        user = User(name=name, email=email, phone=phone, address=address)
        user.save()
        self.stdout.write(f'{user}')
