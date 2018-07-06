from rest_framework import serializers
from .models import Employee
from ..user.serializer import AccountDetailSerializer
from ..user.models import Account


class EmployeeSerializer(serializers.ModelSerializer):

    """
    This serializer class shows the attributes required to display of the Employee object
    In this case all the fields are shown
    """

    account = AccountDetailSerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):

    """
     This serializer class defines how to create a Employee instance
    """

    email = serializers.EmailField(allow_blank=False)
    username = serializers.CharField(max_length=100, allow_blank=False)
    password = serializers.CharField(max_length=100, allow_blank=False)
    user_type = serializers.CharField(max_length=100, allow_blank=False)
    firstname = serializers.CharField(max_length=100, allow_blank=False)
    lastname = serializers.CharField(max_length=100, allow_blank=False)
    phone_number = serializers.CharField(max_length=10, allow_blank=False)
    business = serializers.CharField(max_length=10, allow_blank=False)
    role = serializers.CharField(max_length=10, allow_blank=False)



    class Meta:
        model = Employee
        fields = ('email','username', 'password', 'user_type','firstname', 'lastname', 'phone_number', 'role', 'business',)

    def create(self, validated_data):
            return Account.objects.create_user(**validated_data)


class EmployeeRetrieveUpdateSerial(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        print(account)
        acc = Account.objects.filter(instance.account.id).update_or_create(account)
        return acc



