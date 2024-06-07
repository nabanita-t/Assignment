# from datetime import time


class ApplicationMessages:
    """Project wise generic response messages"""

    # USER Login and Signup
    REQUEST_SENT = "Friend Request sent"
    REQUEST_N_SENT = "Friend Request could not be sent"
    PROFILE_N_EXIST = "Complete your profile first"
    REQUEST_EXIST = "You cannot send more than 3 requests within 1 minute"
    USER_ALREADY_EXIST = "User with this email already Exist!"
    CURRENT_PASSWORD_INCORRECT = "Current password is incorrect"
    WRONG_EMAIL_PASSWORD = "The password you entered is incorrect. Please try again."

    SUCCESS = "Success"

    COMPLETE_PASSWORD_VALIDATION = (
        "Minimum length of password is 8, Maximum length of password is 24 and contain "
        "one Upper Case, one Lower Case and a Special Character and No Spaces"
    )


class Constant:
    """Constants Values"""
    APPROVED = "APPROVED"
    ACCEPTED = "ACCEPTED"
    CREATED = "CREATED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"

    # Gender
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"

    WEB = "WEB"
    ANDROID = "MOBILE"
    IOS = "IOS"


class OnBoardingMessages(object):
    LOGIN_SUCCESS = "Login success"
    LOGIN_FAILED = "Login failed"
    USER_DOES_NOT_EXISTS = "User with this Email doesn't Exist"
    INVALID_PHONE = "Invalid Phone Number"
    INCORRECT_PASSWORD = "Wrong Password"
    PHONE_NUMBER_UPDATED_SUCCESSFULLY = "Phone Number Registered Successfully"


messages = OnBoardingMessages()

