from collections import OrderedDict

from rest_framework import serializers

from .models import Inventory


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class ListCreateSerial(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            merchant = request.user
        return Inventory.objects.create(merchant=merchant, **validated_data)