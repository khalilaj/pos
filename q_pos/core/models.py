from django.db import models
from django.utils.translation import ugettext_lazy as _


class StrictTimestamp(models.Model):
    created_at = models.DateTimeField(_('date joined'), auto_now=True)
    updated_on = models.DateTimeField(_('date modified'), auto_now_add=True)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_on']
