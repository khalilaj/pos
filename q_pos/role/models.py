from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..user.models import Account
from ..business.models import Business
from ..core.models import StrictTimestamp

class Role(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=None, blank=False)
    business = models.ForeignKey(Business, on_delete=None, blank=False)
    name = models.CharField(max_length=30, blank=False)

    #Customer Permissions
    create_customer = models.BooleanField(default=False)
    edit_customer = models.BooleanField(default=False)
    read_customer = models.BooleanField(default=False)
    delete_customer = models.BooleanField(default=False)

    #Role Permissions
    create_role = models.BooleanField(default=False)
    edit_role = models.BooleanField(default=False)
    read_role = models.BooleanField(default=False)
    delete_role = models.BooleanField(default=False)

    #employee Permissions
    create_employee = models.BooleanField(default=False)
    edit_employee = models.BooleanField(default=False)
    read_employee = models.BooleanField(default=False)
    delete_employee = models.BooleanField(default=False)

    #product Permissions
    create_product = models.BooleanField(default=False)
    edit_product = models.BooleanField(default=False)
    read_product = models.BooleanField(default=False)
    delete_product = models.BooleanField(default=False)

    #sale Permissions
    create_sale = models.BooleanField(default=False)
    edit_sale = models.BooleanField(default=False)
    read_sale = models.BooleanField(default=False)
    delete_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')
        unique_together = ('merchant', 'business', 'name',)
