
from rest_framework import serializers

from .models import Product


class ProductRetrieveSerial(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('id', 'merchant',)

class ProductListSerial(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('id', 'merchant',)
        extra_kwargs = {'isQuantified': {'write_only': True}}

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            merchant = request.user
        return Product.objects.create(merchant=merchant, **validated_data)
