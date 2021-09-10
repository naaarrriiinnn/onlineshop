from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required


# خرید را در صورت وارد شدن کاربر به سایت با اطلاعات انجام می پذیرد
@login_required
def cart_add(request, product_id, product_qty=None):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=obj, product=product)
    item.price = product.price
    if (itemCreated == False):
        item.quantity = item.quantity + 1
    obj.items.add(item)
    item.save()
    obj.save()
    return redirect('cart:cart_detail')

# این تابع تعداد خرید ها را بررسی و مورد عمل قرار می دهد
@login_required
def cart_add_q(request, product_id, product_qty=None):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=obj, product=product)
    item.price = product.price
    item.quantity = request.GET['q']
    if request.GET['q'] == "0":
        item.delete()
    else:
        obj.items.add(item)
        item.save()
        obj.save()
    return redirect('cart:cart_detail')


# با این فانکشن انچه به سبد خرید اضافه شده می تواند حذف گردد
def cart_remove(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cartItems = CartItem.objects.filter(cart=obj, product=product)
    cartItems.delete()
    return redirect('cart:cart_detail')

# جزییات سبد خرید نمایش داده می شود
@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
