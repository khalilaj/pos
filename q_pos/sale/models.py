from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..core.models import StrictTimestamp
from ..product.models import Product
from ..user.models import Account
from ..business.models import Business


class Sale(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)

    total = models.FloatField(blank=False)
    discount = models.FloatField(blank=False)
    paid = models.FloatField(blank=False)
    change = models.FloatField(blank=False)
    complete = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('sale')
        verbose_name_plural = _('sales')


class SaleProduct(StrictTimestamp):

    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)
    sale = models.ForeignKey(Sale, blank=False,  on_delete=models.CASCADE, related_name='products')

    productId = models.ForeignKey(Product, on_delete=None,blank=False)
    quantity = models.FloatField(blank=False)
    total = models.FloatField(blank=False)

    class Meta:
        verbose_name = _('sale-product')
        verbose_name_plural = _('sale-products')
