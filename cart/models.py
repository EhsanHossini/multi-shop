from django.db import models
from accounts.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.number}, {self.created_at}"

    class Meta:
        verbose_name = "سبد"
        verbose_name_plural = "سبدها"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    size = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()


class DiscountCode(models.Model):
    name = models.CharField(max_length=7, verbose_name="کد تخفیف", unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name}, {self.discount}'

    class Meta:
        verbose_name = "کد تخفیف کاربران"
        verbose_name_plural = "کد تخفیف"
