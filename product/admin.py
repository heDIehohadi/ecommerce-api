from django.contrib import admin
from .models import (
    StoreCategory,
    StoreProduct,
    StoreComment,
    StoreProductImage,
)
@admin.register(StoreCategory)
class AdminStoreCategory(admin.ModelAdmin):
    pass
@admin.register(StoreComment)
class AdminStoreComment(admin.ModelAdmin):
    pass
@admin.register(StoreProduct)
class AdminStoreProduct(admin.ModelAdmin):
    pass
@admin.register(StoreProductImage)
class AdminProductImage(admin.ModelAdmin):
    pass
