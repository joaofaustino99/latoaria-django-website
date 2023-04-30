from django.urls import include, path
from . import views

app_name = 'store'

urlpatterns = [
 path("", views.index, name="index"),
 path("login/", views.login_page, name="login"),
 path("login/view/", views.loginview, name="loginview"),
 path("logout", views.logoutview, name="logout"),
 path("products/", views.products_view, name="products"),
 path("register/", views.register_page, name="register"),
 path("shop_cart/", views.shop_cart, name="shop_cart"),
 path("shop_cart/delete_<int:item_id>", views.delete_from_cart, name="delete"),
 path("shop_cart/checkout", views.checkout, name="checkout"),
 path("shop_cart/checkout/payment", views.payment, name="payment"),
 path('products/<int:product_id>', views.product_view, name='product_view'),
 path('products/<int:product_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),


]
