from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from ..user.models import Account
from ..core.models import StrictTimestamp


class Business(StrictTimestamp):
    merchant = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=30, blank=False)
    nickname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=False)
    location = models.CharField(max_length=30, blank=True)
    logo = models.FileField(verbose_name='business-logo', name=None, blank=True)

    def create_business(sender, weak=False, **kwargs):
        if kwargs['created']:
            user_type = kwargs['instance'].user_type
            if user_type == 'MC':
                business = Business.objects.create(merchant=kwargs['instance'], name=kwargs['instance'].firstname, email=kwargs['instance'].email)

    post_save.connect(create_business, sender=Account, )


    class Meta:
        verbose_name = _('business')
        verbose_name_plural = _('business')
        unique_together = ('merchant', 'name', 'nickname',)


    def __str__(self):
        return "<Business name={} merchant={}>".format(self.name, self.merchant.firstname)

