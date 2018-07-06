from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp
from django.db.models.signals import post_save
from ..user.models import Account


class Employee(StrictTimestamp):
    account = models.ForeignKey(Account, blank=False, on_delete=None)
    role = models.CharField(blank=True, max_length=40)
    business = models.CharField(blank=True, max_length=40)

    def create_employee(sender, weak=False, **kwargs):
        if kwargs['created']:
            user_type = kwargs['instance'].user_type
            if user_type == 'EMP':
                employee = Employee.objects.create(account=kwargs['instance'])

    post_save.connect(create_employee, sender=Account,)

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employee')

    def __str__(self):
        return "<Employee firstname={} lastname={}>".format(self.account.firstname, self.account.lastname)