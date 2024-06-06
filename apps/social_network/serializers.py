from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.common.constants import ApplicationMessages, Constant
from apps.user import models as user_models
from apps.social_network import models as social_network_model
from apps.social_network import helpers
from django.db import transaction
import datetime
from datetime import datetime, timedelta


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
        user.last_login = datetime.now()
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


class FriendRequestSendSerializer(serializers.ModelSerializer):
    """Send Friend Request"""
    status = serializers.CharField(required=False)

    class Meta:
        model = social_network_model.FriendRequest
        fields = ("to_user", "status")

    def validate(self, attrs):
        """will check if profile of the user exists,and attach id to payload"""
        if not self.instance:
            profile = social_network_model.Profile.objects.filter(user=self.context.get("user"))
            if not profile.exists():
                raise serializers.ValidationError(ApplicationMessages.PROFILE_N_EXIST)
            # Check if 3 requests were sent in last 1 minute
            end_time = datetime.now()
            start_time = end_time - timedelta(minutes=1)
            friend_requests = social_network_model.FriendRequest.objects.filter(from_user__user=self.context.get("user"),
                                                                                created_at__range=(
                                                                                start_time, end_time))
            # Restrict user from sending more than 3 requests in 1 minute
            if friend_requests.count() >= 3:
                raise serializers.ValidationError(ApplicationMessages.REQUEST_EXIST)
            attrs["from_user"] = profile.get()
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        """Send Friend Request"""
        validated_data["status"] = Constant.PENDING
        profile = social_network_model.FriendRequest.objects.create(**validated_data)
        return profile

    @transaction.atomic
    def update(self, instance, validated_data):
        """Update Friend Request status"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class FriendRequestListSerializer(serializers.ModelSerializer):
    """List Friend Request"""
    to_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = social_network_model.FriendRequest
        fields = ("id", "to_user", "status")

    def get_to_user(self, obj):
        if obj.to_user:
            return obj.to_user.first_name + " " + obj.to_user.last_name
        return None


class UserListSerializer(serializers.ModelSerializer):
    """List of all Users Serializer"""
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = social_network_model.Profile
        fields = ("id", "first_name", "last_name", "gender", "email")

    def get_email(self, obj):
        if obj.user:
            return obj.user.email
        return None
