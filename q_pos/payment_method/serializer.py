from collections import OrderedDict
from rest_framework import serializers
from .models import PaymentMethod


class PaymentMethodRetrieveSerial(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'
        read_only_fields = ("id", "merchant",)

class PaymentMethodListSerial(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = "__all__"
        read_only_fields = ("id", "merchant", )

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            merchant = request.user
        return PaymentMethod.objects.create(merchant=merchant, **validated_data)
