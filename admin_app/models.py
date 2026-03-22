from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_type = models.CharField(max_length=20)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    usage_limit = models.IntegerField()
    used_count = models.IntegerField(default=0)

class OfferDiscountBridge(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

class ProductOfferBridge(models.Model):
    product = models.ForeignKey("seller.Product", on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

class CategoryOfferBridge(models.Model):
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

class ProductDiscountBridge(models.Model):
    product = models.ForeignKey("seller.Product", on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

class CategoryDiscountBridge(models.Model):
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

class PlatformCommission(models.Model):
    seller = models.ForeignKey("seller.SellerProfile", on_delete=models.CASCADE)
    order_item = models.ForeignKey("customer.OrderItem", on_delete=models.CASCADE)
    commission_percentage = models.FloatField()
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    settlement_status = models.CharField(max_length=20)
    settled_at = models.DateTimeField(null=True, blank=True)

class Deal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    banner_image = models.ImageField(upload_to='deal_images/', blank=True, null=True, help_text="Banner image for the deal section")
    products = models.ManyToManyField("seller.Product", related_name="deals")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount percentage (e.g., 20 for 20%)")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Deal"
        verbose_name_plural = "Deals"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_currently_active(self):
        from django.utils import timezone
        now = timezone.now()
        return self.is_active and self.start_date <= now <= self.end_date