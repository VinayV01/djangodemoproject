




from django.urls import path
from shop import views

app_name="shop"
urlpatterns = [
    path('',views.categories,name="categories"),
    path('products/<int:i>',views.products,name="products"),
    path('detail/<int:i>',views.productdetail,name="detail"),
    path('register',views.register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('addcategories',views.addcategories,name="addcategories"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('addstock/<int:i>',views.addstock,name="addstock")
]
