from collections import OrderedDict
from rest_framework import serializers
from .models import Role


class RoleRetrieveSerial(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ("id", "merchant",)

class RoleListSerial(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = ("id", "merchant", )

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            merchant = request.user
        return Role.objects.create(merchant=merchant, **validated_data)
