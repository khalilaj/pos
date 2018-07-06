from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..user.models import Account
from ..business.models import Business
from ..core.models import StrictTimestamp

class Customer(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
