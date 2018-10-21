from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..user.models import Account
from ..business.models import Business
from ..core.models import StrictTimestamp


class Category(StrictTimestamp):
    name = models.CharField(max_length=30, blank=False)
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return "<Category name={} business={}>".format(self.name, self.business.name)
