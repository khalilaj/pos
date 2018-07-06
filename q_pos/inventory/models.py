from django.db import models
from django.utils.translation import ugettext_lazy as _
from .signals import *
from ..user.models import Account
from ..business.models import Business
from ..core.models import StrictTimestamp
from ..product.models import Product


class Inventory(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None)
    business = models.ForeignKey(Business, on_delete=None, blank=False)
    product = models.ForeignKey(Product, on_delete=None, blank=False)
    quantity = models.FloatField(default=0)

    class Meta:
        verbose_name = _('inventory')
        verbose_name_plural = _('inventory')
        unique_together = ('merchant', 'business', 'product',)

    def __str__(self):
        return "<Inventory id={}, product={}, quantity={}>".format(self.id,self.product.name, self.quantity)
