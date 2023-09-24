from django.urls import path

from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.fetch_order_by_id, name='order-detail'),
    path('orders/average_product_count/', views.fetch_average_product_count, name='fetch_average_product_count'),
    path('products/<int:product_id>/average_product_quantity/', views.fetch_average_product_quantity, name='fetch_average_product_quantity'),
]

