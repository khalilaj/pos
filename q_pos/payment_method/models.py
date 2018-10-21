from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..user.models import Account
from ..business.models import Business
from ..core.models import StrictTimestamp


class PaymentMethod(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)
    payment_name = models.CharField(max_length=30, blank=False)

    class Meta:
        verbose_name = _("Payment Method")
        verbose_name_plural = _("Payment Methods")
        unique_together = ("merchant", "business", "payment_name")

    def __str__(self):
        return "<PaymentMethod payment_name={} business={}>".format(
            self.payment_name, self.business.name
        )
