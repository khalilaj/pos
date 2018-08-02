from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..business.models import Business
from ..category.models import Category
from ..core.models import StrictTimestamp
from ..user.models import Account


class Product(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business,default=1, on_delete=None, blank=False)

    name = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey(Category, on_delete=None)
    unit_price = models.FloatField(default=0, blank=True)
    sale_price = models.FloatField(default=0)
    isQuantified = models.BooleanField(default=False, blank=True)
    currentStock= models.IntegerField(default=False, blank=True)
    minStock = models.IntegerField(default=False, blank=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return "<Product name={} {}>".format(self.name, self.isQuantified)

