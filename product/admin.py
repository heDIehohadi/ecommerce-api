from django.contrib import admin
from .models import (
    StoreCategory,
    StoreComment,
    StoreProduct,
    StoreProductImage,
)


@admin.register(StoreCategory)
class AdminStoreCategory(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(StoreComment)
class AdminStoreComment(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating')
    list_filter = ('rating',)
    ordering = ('-id',)


@admin.register(StoreProduct)
class AdminStoreProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'sku', 'category')
    search_fields = ('name', 'sku')
    list_filter = ('category',)
    ordering = ('-id',)


@admin.register(StoreProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ('product', 'id')