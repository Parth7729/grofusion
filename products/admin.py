from django.contrib import admin
from .models import Product, MainCategory, Category, SubCategory, Brand, ProductSize, ProductGallery, Color

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'id', 'supplier', 'main_category')

class CommonDisplay(admin.ModelAdmin):
    list_display = ('name', 'value')

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'value')

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'color')

admin.site.register(Product, ProductAdmin)
admin.site.register(MainCategory, CommonDisplay)
admin.site.register(Category, CommonDisplay)
admin.site.register(SubCategory, CommonDisplay)
admin.site.register(Brand, CommonDisplay)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductGallery, ProductGalleryAdmin)
admin.site.register(Color, CommonDisplay)