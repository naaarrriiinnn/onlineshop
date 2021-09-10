from django.db import models
from shop.models import Product
from accounts.models import User


#  مدل کلی سفارشات ارایه شده است
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} {}'.format(self.user, self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


# جهت جلئوگیری از افزونگی در دیتابیس جدول میانی زیر تشکیل شده و هزینه در ان محاسبه گشته
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,
                              related_name='order_items',
                              on_delete=models.CASCADE,
                              )
    product = models.ForeignKey(Product,
                                related_name='order_products',
                                on_delete=models.CASCADE,
                                )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
