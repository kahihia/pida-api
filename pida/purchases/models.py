from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        (1, 'Preparing'),
        (2, 'Shipping'),
        (3, 'Delivered'),
    )

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='purchase_orders')
    items = models.ManyToManyField('PurchaseItem',
                                   related_name='+')
    order_time = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_CHOICES[0][0])

    def is_valid(self):
        if self.status not in [c[0] for c in self.STATUS_CHOICES]:
            return False
        if self.items.count() == 0:
            return False
        if self.price != sum(i.product.price*i.number for i in self.items.all()):
            return False
        if self.items.all().count() != len(set([i.product for i in self.items.all()])):
            return False
        if any(i.number==0 for i in self.items.all()):
            return False
        return True


class PurchaseItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='+')
    number = models.PositiveSmallIntegerField()