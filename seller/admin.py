from django.contrib import admin
from .models import (
    SellerProfile,
    Product,
    ProductVariant,
    ProductImage,
    InventoryLog,
)

admin.site.register(SellerProfile)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)
admin.site.register(InventoryLog)