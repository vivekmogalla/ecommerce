from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    measurement = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_count = models.IntegerField()

    def __str__(self):
        return f"Order ID: {self.order_id}, Product Count: {self.product_count}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order ID: {self.order.order_id}, Product: {self.product.name}, Quantity: {self.quantity}"
