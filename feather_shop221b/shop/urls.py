from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('', include('shop.urls')) , #اضافه کردن آدرس های اپلیکیشن
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_view, name='cart'),

]
