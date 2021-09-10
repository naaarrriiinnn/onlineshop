from django.shortcuts import render, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt


# در این بخش با در نظر گرفتن امنیت عملیات پرداخت به اتمام می رسد
@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


# در این بخش با در نظر گرفتن امنیت عملیات پرداخت به منحل کی گردد
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
