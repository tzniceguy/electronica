from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('discounted-products/', views.discount_product, name="discounted-products"),
    path('auth/', views.auth, name='authorization'),
]
