from collections import OrderedDict
from rest_framework import serializers
from .models import Category


class CategoryRetrieveSerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "business")
        read_only_fields = ("id", "merchant")


class CategoryListSerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "business")
        read_only_fields = ("id", "merchant")

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")

        if request and hasattr(request, "user"):
            merchant = request.user
        return Category.objects.create(merchant=merchant, **validated_data)
