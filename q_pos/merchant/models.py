from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp
from django.db.models.signals import post_save
from ..user.models import Account


class Merchant(StrictTimestamp):
    account = models.OneToOneField('Account', blank=False, on_delete= None)

    def create_merchant(sender,weak=False,**kwargs):
        if kwargs['created']:
            user_type = kwargs['instance'].user_type
            if user_type == 'MC':
                merchant = Merchant.objects.create(account=kwargs['instance'])

    post_save.connect(create_merchant, sender=Account,)

    class Meta:
        verbose_name = _('merchant')
        verbose_name_plural = _('merchants')

    def __str__(self):
        return "<Merchant firstname={} lastname={}>".format(self.account.firstname, self.account.lastname)