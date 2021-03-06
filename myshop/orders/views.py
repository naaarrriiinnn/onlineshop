from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import *
from cart.models import Cart
from accounts.models import Profile


# Create your views here.

# سفارشات با در نظر گرفته شدن اطلاعات کاربر ذخیره میگردد
def order_save(request):
    order = Order.objects.create(user=request.user)
    cart = Cart.objects.get(user=request.user)
    order.save()
    for item in cart.items.all():
        orderItem, created = OrderItem.objects.update_or_create(
            order=order, product=item.product, price=item.price, quantity=item.quantity)
        order.order_items.add(orderItem)
    order.address = request.POST['address']
    order.postal_code = request.POST['zip']
    order.country = request.POST['country']
    order.state = request.POST['state']
    order.save()
    return redirect('../../payment/' + str(order.id) + '/process')


# سفارش متناسب با کاربر ساخته می شوند
def order_create(request):
    profile = get_object_or_404(Profile, user=request.user)
    cart = Cart.objects.get(user=request.user)
    return render(request, 'orders/order_list.html', {'cart': cart, 'profile': profile})
