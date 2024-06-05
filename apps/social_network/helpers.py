from apps.common.constants import ApplicationMessages, messages
from rest_framework.exceptions import ValidationError
import re
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
import socket
from apps.user import models as user_models
import datetime
from rest_framework.response import Response
from rest_framework import status


def password_validator(password):
    """will validate the password and raise validation error if necessary"""

    if (
            len(password) < 8
            or len(password) > 25
            or re.search("^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$", password)
            or " " in password
    ):
        raise ValidationError(ApplicationMessages.COMPLETE_PASSWORD_VALIDATION)


def create_user_session(device, user):
    """get data and create session"""
    # try:
    user = user_models.User.get_instance({"id": user})
    access_token = OutstandingToken.objects.filter(user=user).order_by(
        "-created_at"
    )[0]
    user_session_info = {
        "ip": socket.gethostbyname(socket.gethostname()),
        "user": user,
        "token": access_token,
    }
    if device:
        user_session_info["device_token"] = device.get("device_token")
        user_session_info["device_type"] = device.get("device_type")
    user_ses = user_models.UserSessionInfo.create_instance(user_session_info)
    return user_ses
    # except Exception:
    #     raise ValidationError(ApplicationMessages.SOMETHING_WENT_WRONG)


def login_user(data):
    """User login via email and password and return token"""
    email = data.get("email").lower()
    password = data.get("password")
    user = user_models.User.get_instance({"email": email})
    if password and user.check_password(password):
        response = {
            "message": messages.LOGIN_SUCCESS,
            "tokens": user.tokens(),
            "email": user.email,
            "user_id": user.id
        }
        user.last_login = datetime.datetime.now()
        user.save()
        user_ses = create_user_session(data.get("device"), user.id)
        response["session_id"] = user_ses.id
        return {"response": Response(data=response, status=status.HTTP_200_OK)}
    else:
        return {
            "response": Response(
                data=ApplicationMessages.WRONG_EMAIL_PASSWORD,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        }
