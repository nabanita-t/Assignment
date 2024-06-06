from django.urls import path, include
from apps.social_network import views

app_name = "social_network"
# prefixes = /customer/
urlpatterns = [
    path('register', views.UserRegisterAPIView.as_view(), name="register-user"),
    path('login', views.UserLoginAPIView.as_view(), name="login-user"),
    path('request', views.SendFriendRequestAPIView.as_view(), name="send-request"),
    path('request/<uuid:request_id>', views.FriendRequestDetailsAPIView.as_view(), name="request-details"),
    path('user-list', views.AllUserAPIView.as_view(), name="user-list"),
]
