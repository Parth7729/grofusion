from django.urls import path
from . import views

urlpatterns = [
    path('product-listing/add-product/adding-product/', views.adding_product, name='adding-product'),
    path('product-listing/status-change/<int:id>/', views.status_change, name='status-change'),
    path('product-listing/delete-product/<int:id>/', views.delete_product, name='delete-product'),
    path('product-listing/update-product/<int:id>/', views.update_product, name='update-product'),
    path('product-listing/delete-photo-gallery/<int:id>/', views.delete_photo_gallery, name='delete-photo-gallery'),
    path('product-details/<str:category>/<str:product_name>/', views.product_details, name='product-details'),
    # path('<category>/', views.category_products, name='products-by-category'),
]