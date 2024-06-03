from django.core.validators import MinValueValidator
from apps.common.models import BaseModel
from django.db import models
from rest_framework.validators import ValidationError
from rest_framework import status
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.common.constants import ApplicationMessages, Constant
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


class MyUserManager(BaseUserManager):
    """The Custom BaseManager Class"""

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    """ The user Model for storing emails, password and permissions """

    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)  # Django Active User
    is_admin = models.BooleanField(default=False)  # Django Admin

    token_version = models.IntegerField(default=1, validators=[MinValueValidator(1), ], editable=False)
    last_login = models.DateTimeField(null=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-created_at']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        # Get Outstanding Token Object
        token = OutstandingToken.objects.get(token=str(refresh))

        # Add custom claims
        refresh['token_version'] = self.token_version
        token.token = str(refresh)
        token.save()

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    @staticmethod
    def get_user(filters):
        try:
            user = User.objects.get(**filters)
            return user
        except User.DoesNotExist:
            raise ValidationError(ApplicationMessages.USER_NOT_EXISTS, status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update_password(user_id, new_password, old_password=None):
        try:
            obj = User.objects.get(id=user_id)
            if new_password and obj.check_password(old_password):
                obj.set_password(new_password)
                obj.save()
                return obj
            else:
                raise ValidationError(ApplicationMessages.CURRENT_PASSWORD_INCORRECT, status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            raise ValidationError(ApplicationMessages.USER_NOT_EXISTS, status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def create_user(email, password=None):
        data = {"email": email, "password": password}
        instance = User(**data)
        instance.set_password(password)
        instance.save()
        return instance

    @staticmethod
    def filter_all_users(filters=None):
        """
        will filter "verified user" and "not-deleted-user" by default
        : excluding Django Admin and soft deleted users
        """
        if not filters:
            user = User.objects.filter(is_admin=False)
        else:
            user = User.objects.filter(**filters, is_admin=False)
        return user

    @staticmethod
    def set_user_password(password=None, user=None):
        user.set_password(password)
        user.save()


class UserSessionInfo(BaseModel):
    """User session info, which include, user device token, ip address, user agent, device type (WEB, ANDROID, IOS),
    is_safari for web only, when user is login then its token is added in jwt tokens we also need to save his session
    in user session info as well, and also at the time of logout delete this particular session"""

    device = (
        (Constant.WEB, Constant.WEB),
        (Constant.ANDROID, Constant.ANDROID),
        (Constant.IOS, Constant.IOS)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.ForeignKey(OutstandingToken, on_delete=models.CASCADE, null=True)
    device_token = models.TextField(null=True)
    device_type = models.CharField(max_length=100, null=True, choices=device)
    is_safari = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        verbose_name = "User Session Info"
        verbose_name_plural = "User Session Info"
        ordering = ["-created_at"]

    def __str__(self):
        """string representation of User session Info model"""
        return "User: {} - Device Type: {}".format(self.user, self.device_type)

