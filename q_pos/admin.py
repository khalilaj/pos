from django.contrib import admin


from .user.models import Account
from .employee.models import Employee
from .business.models import Business
from .role.models import Role
from .category.models import Category
from .product.models import Product
from .sale.models import Sale
from .payment_method.models import PaymentMethod
from .customer.models import Customer
from .inventory.models import Inventory


models = [
            Account,
            Employee,
            Business,
            Category,
            Product,
            Sale,
            Role,
            PaymentMethod,
            Inventory
         ]

admin.site.register(models)


