from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('products/', views.Products.as_view(), name='products'),
    path('products/new', views.ProductsCreate.as_view(), name='products_create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('products/<int:pk>/delete', views.ProductsDelete.as_view(), name="products_delete"),
    path('products/<int:pk>/update', views.ProductsUpdate.as_view(), name='products_update'),

]