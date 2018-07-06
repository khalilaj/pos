from rest_framework import serializers

from ..sale.models import Sale, SaleProduct
from ..product.models import Product
from ..inventory.models import Inventory

class SaleProductSerial(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = ("productId", "quantity", "total")

class SaleRetrieveSerializer(serializers.ModelSerializer):

    products = SaleProductSerial(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ('id', 'business', 'paid', 'change', 'total', 'discount', 'total', 'products')


class SaleListCreateSerializer(serializers.ModelSerializer):

    products = SaleProductSerial(many=True)

    class Meta:
        model = Sale
        fields = ('id','business', 'products', 'paid', 'change', 'total', 'discount', 'total')
        read_only_fields = ('id', 'created_at', 'updated_on')

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")

        # Get the current user
        if request and hasattr(request, "user"):
            merchant = request.user

        business = validated_data['business']
        sale_products = validated_data.pop('products')

        sale = Sale.objects.create(merchant=merchant, **validated_data)

        for product in sale_products:
            # Create a sale product transaction
            # Reference: database schema (Sale, SaleProduct)
            SaleProduct.objects.create(merchant=merchant, business=business, sale=sale, **product)

            productObj = product['productId']
            soldQuantity = product['quantity']
            print(productObj)
            # # Check if product is quantify-able
            if productObj.isQuantified:
                # Decrement Inventory if true
                inventory = Inventory.objects.get(merchant=merchant, business=business, product=productObj)
                #Get current product quantity
                q = inventory.quantity
                #change the quantity by decrementing the sold product quantity
                inventory.quantity = q - soldQuantity
                #save the inventory instance
                inventory.save()




        return sale
