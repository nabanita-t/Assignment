from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.common.constants import ApplicationMessages, Constant
from apps.user import models as user_models
from apps.social_network import models as social_network_model
from apps.social_network import helpers
from django.db import transaction
import datetime


class UserSessionSerializer(serializers.Serializer):
    """serializer for taking user session info which include, device token, device type, is_safari"""

    device_choice = (
        (Constant.IOS, Constant.IOS),
        (Constant.ANDROID, Constant.ANDROID),
        (Constant.WEB, Constant.WEB),
    )

    device_token = serializers.CharField()
    device_type = serializers.ChoiceField(choices=device_choice)
    is_safari = serializers.BooleanField(default=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer to register any user and create their profile"""

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    phone = serializers.CharField(required=False)
    country_code = serializers.CharField(required=False)
    device = UserSessionSerializer(write_only=True, required=False)

    class Meta:
        model = social_network_model.Profile
        fields = ("email", "password", "first_name", "last_name", "gender", "phone", "country_code",
                  "device")

    def validate(self, data):
        """Function to check if the email is already registered"""

        # Check if email is already registered with us
        user = user_models.User.objects.filter(email__iexact=data['email'])
        if user.exists():
            raise serializers.ValidationError(f"{ApplicationMessages.USER_ALREADY_EXIST}")
        return data

    @transaction.atomic
    def create(self, validated_data):
        """User register serializer"""
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        helpers.password_validator(password)
        user = user_models.User.create_user(email=email, password=password)
        validated_data['user'] = user
        profile = social_network_model.Profile.objects.create(**validated_data)

        response = {
            "user_id": user.id,
            "profile_id": profile.id,
            "tokens": user.tokens(),
            "device": validated_data.get("device", None)
        }
        user.last_login = datetime.datetime.now()
        user.save()
        return response


class UserLoginSerializer(serializers.Serializer):
    """User Login serializer"""

    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    device = UserSessionSerializer(write_only=True, required=False)

    def validate(self, attrs):
        """will convert email to lower case to avoid duplication issue"""
        attrs["email"] = attrs.get("email").lower()
        return attrs
