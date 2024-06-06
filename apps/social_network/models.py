from django.db import models
from apps.common.models import BaseModel
from apps.user.models import User
from apps.common.constants import Constant


class Profile(BaseModel):
    """
    Profile model to store personal data
    """

    GENDER_CHOICE = (
        (Constant.MALE, Constant.MALE),
        (Constant.FEMALE, Constant.FEMALE),
        (Constant.OTHERS, Constant.OTHERS)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country_code = models.CharField(max_length=16, null=True, blank=True)
    gender = models.CharField(max_length=16, blank=True, null=True, choices=GENDER_CHOICE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Email: {} - Name: {} {}'.format(self.user, self.first_name, self.last_name)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['-created_at']


class FriendRequest(BaseModel):
    """
    Friend Request model to store data related to friend requests
    """

    request_status_choices = (
        (Constant.PENDING, Constant.PENDING),
        (Constant.ACCEPTED, Constant.ACCEPTED),
        (Constant.REJECTED, Constant.REJECTED),
    )

    from_user = models.ForeignKey("social_network.Profile", on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='from_user')
    to_user = models.ForeignKey("social_network.Profile", on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='to_user')
    status = models.CharField(choices=request_status_choices, max_length=16, default=Constant.PENDING)

    def __str__(self):
        """String for Friend Request"""
        return "From:{} -To:{}".format(self.from_user.first_name, self.to_user.first_name)

    class Meta:
        verbose_name = "Friend Request"
        verbose_name_plural = "Friend Requests"
        unique_together = ("from_user", "to_user")
        ordering = ['-created_at']
