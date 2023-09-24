from django.shortcuts import render
from django.db.models import Avg
from django.http import JsonResponse
from .models import Order, Product, OrderProduct

# Create your views here.


def fetch_order_by_id(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        order_products = OrderProduct.objects.filter(order=order)

        data = {
            'order_id': order.order_id,
            'product_count': order.product_count,
            'products': [
                {
                 'id': order_product.product.id,
                    'name': order_product.product.name,
                    'measurement': order_product.product.measurement,
                    'quantity': order_product.quantity
                }
                for order_product in order_products
            ]
        }
        return JsonResponse(data)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)


def fetch_average_product_count(request):
    average_product_count = Order.objects.aggregate(
        avg_product_count=Avg('product_count')).get('avg_product_count')
    return JsonResponse({'average_product_count': average_product_count})


def fetch_average_product_quantity(request, product_id):
    average_product_quantity = OrderProduct.objects.filter(
        product_id=product_id).aggregate(avg_quantity=Avg('quantity'))
    return JsonResponse({'average_product_quantity': average_product_quantity})