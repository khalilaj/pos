from django.contrib.auth import authenticate
from rest_framework import serializers


from .models import Account
from .exception import UserNotFound, NoEmailProvided, UserNotActive


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Describes how a user can register to QUICKIE
    """

    password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Account

        fields = (
            "email",
            "username",
            "password",
            "user_type",
            "token",
            "id",
            "firstname",
            "lastname",
            "phone_number",
        )

    def create(self, validate_data):
        return Account.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    """
    Describes how a user can log in to QUICKIE
    """

    id = serializers.CharField(max_length=128, read_only=True)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        Validates the data passed to the login/
        """

        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise NoEmailProvided

        account = authenticate(email=email, password=password)

        if account is None:
            raise UserNotFound

        if not account.is_active:
            raise UserNotActive

        return {
            "id": account.id,
            "email": account.email,
            "user_type": account.user_type,
            "token": account.token,
            "firstname": account.firstname,
            "lastname": account.lastname,
            "phone_number": account.phone_number,
            "username": account.username,
        }

    class Meta:
        model = Account
        fields = (
            "id",
            "email",
            "password",
            "user_type",
            "username",
            "firstname",
            "lastname",
            "phone_number",
            "token",
        )
        read_only_fields = (
            "id",
            "token",
            "user_type",
            "username",
            "firstname",
            "lastname",
            "phone_number",
        )


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "username",
            "password",
            "token",
            "user_type",
            "phone_number",
            "firstname",
            "lastname",
        )
        read_only_fields = ("token",)

    def update(self, instance, validate_data):
        password = validate_data.pop("password", None)

        for (key, value) in validate_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "id",
            "firstname",
            "lastname",
            "email",
            "username",
            "user_type",
            "phone_number",
        )


class AccountEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
