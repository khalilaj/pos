from django.dispatch import receiver
from django.db.models.signals import post_save
from django.apps import apps

from ..product.models import Product

@receiver(post_save, sender=Product)
def ensure_inventory_exists(sender, **kwargs):

    from .models import Inventory
    model = apps.get_model('q_pos', 'Inventory', require_ready=True)

    created = kwargs.get('created', None)
    instance = kwargs.get('instance', None) # instance is Product object

    business = instance.business
    merchant = instance.merchant

    if created and instance.isQuantified:
        return Inventory.objects.get_or_create(merchant=merchant, business=business, product=instance)
