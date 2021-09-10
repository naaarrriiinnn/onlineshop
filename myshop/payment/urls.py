from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [

    path('canceled/$', views.payment_canceled, name='canceled'),
    path('done/$', views.payment_done, name='done'),

]
