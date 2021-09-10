from django.db import models
from accounts.models import User
from shop.models import Product


# مدل لیست خرید بعدش ارایه شده است
class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'wishlist of {}'.format(self.user.email)


# جهت پیشگریر یاز افزونگی جدول میانی زیر ارایه شده است
class WishlistItem(models.Model):
    id = models.AutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist,related_name='wishlist_items',null=True,on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='wishlist_item',on_delete=models.CASCADE,)

    def __str__(self):
        return '{}'.format(self.product.name)
