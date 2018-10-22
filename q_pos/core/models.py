from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import _get_queryset
from q_pos.core.exceptions import ResourceDoesNotExist

class StrictTimestamp(models.Model):
    created_at = models.DateTimeField(_("date joined"), auto_now=True)
    updated_on = models.DateTimeField(_("date modified"), auto_now_add=True)

    class Meta:
        abstract = True

        ordering = ["-created_at", "-updated_on"]

def get_or_raise(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    if not hasattr(queryset, 'get'):
        klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError(
            "First argument to get_or_raise() must be a Model, Manager, "
            "or QuerySet, not '%s'." % klass__name
        )
    
    error_msg = kwargs.pop("error_msg", "")
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise ResourceDoesNotExist(error_msg)