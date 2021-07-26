from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product-listing/', views.product_listing, name='product-listing'),
    path('add-product/', views.add_product, name='add-product'),
    path('search-results/', views.search, name='search'),
    path('product-enquiry/', views.product_enquiry, name='product-enquiry'),
    path('for-buyers/', views.for_buyers, name='for-buyers'),
    path('for-suppliers/', views.for_sellers, name='for-sellers'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('affiliate-program/', views.affiliate, name='affiliate-program'),
    path('all-categories/', views.all_categories, name='all-categories'),

    path('<main_category>/', views.category_products, name='products-by-category'),
    path('<main_category>/<category>/', views.category_products, name='products-by-category'),
    path('<main_category>/<category>/<sub_category>/', views.category_products, name='products-by-category'),
]
