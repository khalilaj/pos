from collections import OrderedDict
from rest_framework import serializers
from .models import Customer


class CustomerRetrieveSerial(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ("id", "merchant",)

class CustomerListSerial(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("id", "merchant", )

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            merchant = request.user
        return Customer.objects.create(merchant=merchant, **validated_data)
