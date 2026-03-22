from django.contrib import admin
from .models import (
    Offer,
    Discount,
    Coupon,
    OfferDiscountBridge,
    ProductOfferBridge,
    CategoryOfferBridge,
    ProductDiscountBridge,
    CategoryDiscountBridge,
    PlatformCommission,
    Deal,
)

admin.site.register(Offer)
admin.site.register(Discount)
admin.site.register(Coupon)
admin.site.register(OfferDiscountBridge)
admin.site.register(ProductOfferBridge)
admin.site.register(CategoryOfferBridge)
admin.site.register(ProductDiscountBridge)
admin.site.register(CategoryDiscountBridge)
admin.site.register(PlatformCommission)
admin.site.register(Deal)
# Register your models here.


class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount_percentage', 'is_active', 'start_date', 'end_date']
    list_filter = ['is_active', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    filter_horizontal = ['products']  # For many-to-many field
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'banner_image')
        }),
        ('Deal Settings', {
            'fields': ('products', 'discount_percentage', 'start_date', 'end_date', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# Unregister the default registration and register with custom admin
admin.site.unregister(Deal)
admin.site.register(Deal, DealAdmin)
