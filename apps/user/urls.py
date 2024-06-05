from django.urls import path, include


app_name = "user"
# prefix = /user/
urlpatterns = [
    # path('login/', include([
    #     path('send-otp', user_profile.PhoneNumberLoginAPIView.as_view(), name='send-otp'),
    #     path('verify-otp', user_profile.OTPVerifyAPIView.as_view(), name='verify-otp'),
    # ])),
    # path('forgot-password', user_profile.ForgotPasswordAPIView.as_view(), name="forgot-password"),
    # path('reset-password', user_profile.ResetPasswordLinkAPIView.as_view(), name="reset-link-password"),
    # path('change-password', user_profile.ChangePasswordView.as_view(), name="admin-change-password"),
    # path('logout', user_profile.LogOutAPIView.as_view(), name="logout"),
    # path('update/session/<uuid:session_id>', user_profile.UpdateUserSessionView.as_view(), name="update-user-session"),
    # path('conversation/webhooks', user_profile.SendMessageReceivedPushNotification.as_view(),
    #      name="message-push-notification"),

]
