

from django.urls import path
app_name="cart"

from cart import views


urlpatterns = [
    path('<int:i>',views.addtocart,name="addtocart"),
    path('cartview',views.cart_view,name="cartview"),
    path('cart_remove/<int:i>',views.cart_remove,name="cart_remove"),
    path('cart_fullremove/<int:i>',views.cart_fullremove,name="cart_fullremove"),
    path('orderform',views.orderform,name="orderform"),
    path('payment-status/<str:p>',views.payment_status,name="status"),
    path('orderview',views.orderview,name="orderview"),
]