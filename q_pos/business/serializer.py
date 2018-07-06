from collections import OrderedDict
from rest_framework import serializers
from .models import Business


class RetrieveUpdateSerial(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('id', 'name', 'nickname', 'email', 'location')


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Business
        fields = ('id', 'name', 'nickname', 'email', 'location')
        read_only_fields = ('id',)

    def create(self, validated_data):
        merchant = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):

            merchant = request.user
        return Business.objects.create(merchant=merchant, **validated_data)
