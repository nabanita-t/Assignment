from rest_framework import status, generics, mixins, views, parsers, filters
from rest_framework.response import Response
from apps.social_network import serializers as social_network_serializer
from apps.social_network import helpers


class UserRegisterAPIView(generics.GenericAPIView, mixins.CreateModelMixin):
    """
    API to register a user
    """

    serializer_class = social_network_serializer.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        """create a new user profile"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = serializer.save()
            helpers.create_user_session(response.get("device", None), response.get("user_id", None))
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(generics.GenericAPIView):
    """User Login API"""

    serializer_class = social_network_serializer.UserLoginSerializer

    def post(self, request):
        """Login as well as create a session"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            data = helpers.login_user(
                serializer.validated_data
            )
            return data["response"]
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
