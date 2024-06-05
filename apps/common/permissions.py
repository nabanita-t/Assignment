from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.backends import TokenBackend


def verify_token_version(request):
    """
    We have added this extra Auth check to restrict the users to Invalidate the tokens prior force logging of user.
    Force Logging of Users:
    _______________________
    1. When User Request for Forgot/Reset password.
    2. When We want to block the user (Can be done using default authentication class)
    3. When User permissions Updated (Alternative of force logging out - We can Implement Object Level
    Permissions).
    4. To Force Logout all users or particular user when user account compromised.
    : param request: API Request
    : return: Auth Error / Boolean Value
    """
    try:
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token_version = TokenBackend(algorithm='HS256').decode(token, verify=False).get("token_version")
        if token_version and token_version == request.user.token_version:
            return True
        else:
            raise Exception(f'Token is invalid or expired')
    except Exception as ex:
        raise AuthenticationFailed(ex, status.HTTP_401_UNAUTHORIZED)


class IsUser(BasePermission):
    """User should an active user"""

    @staticmethod
    def user_permission_bool(user):
        """will check related permission Customer"""
        if user.is_active:
            return True
        else:
            return False

    def has_permission(self, request, view):
        return bool(
            not isinstance(request.user, AnonymousUser)
            and verify_token_version(request)
            and IsUser.user_permission_bool(request.user)
        )
