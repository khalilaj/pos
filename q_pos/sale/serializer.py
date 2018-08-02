from rest_framework import serializers

from ..sale.models import Sale, SaleProduct


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
            # # Check if product is quantify-able
            if productObj.isQuantified:
                #Get current product quantity
                q = productObj.currentStock
                # change the quantity by decrementing the sold product quantity
                # Decrement Inventory if true
                productObj.currentStock = q - soldQuantity
                #save the inventory instance
                productObj.save()
            else:
                productObj.currentStock = None
        return sale
