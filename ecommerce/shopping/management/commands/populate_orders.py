import json
from django.core.management.base import BaseCommand
from shopping.models import Order, Product, OrderProduct

class Command(BaseCommand):
    help = 'Populate orders in the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the order data JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as file:
            data = json.load(file)

            for order_data in data['data']:
                order_id = order_data['order_id']
                product_count = order_data['product_count']

                order = Order.objects.create(order_id=order_id, product_count=product_count)

                products = order_data['products']
                for product in products:
                    product_id = product['id']
                    quantity = product['quantity']
                    name = product['name']
                    measurement = product['measurement']

                    try:
                        product_obj, created = Product.objects.get_or_create(id=product_id, defaults={'name': name, 'measurement': measurement})
                    except Product.DoesNotExist:
                        # Handle the case where the product doesn't exist
                        continue

                    OrderProduct.objects.create(order=order, product=product_obj, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('Orders populated successfully'))
