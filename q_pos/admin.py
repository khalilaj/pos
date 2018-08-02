from django.contrib import admin

from .user.models import Account
from .business.models import Business
from .category.models import Category
from .product.models import Product
from .sale.models import Sale
from .payment_method.models import PaymentMethod


models = [
            Account,
            Business,
            Category,
            Product,
            Sale,
            PaymentMethod,
         ]

admin.site.register(models)


