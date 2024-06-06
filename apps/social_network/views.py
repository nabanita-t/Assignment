from rest_framework import status, generics, mixins, views, parsers, filters
from rest_framework.response import Response
from apps.social_network import serializers as social_network_serializer
from apps.social_network import models as social_network_models
from apps.social_network import filters as social_network_filters
from apps.social_network import helpers
from apps.common import permissions, constants, pagination


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


class SendFriendRequestAPIView(generics.GenericAPIView):
    """Send Friend Request"""

    serializer_class = social_network_serializer.FriendRequestSendSerializer
    permission_classes = (permissions.IsUser,)
    filter_backends = (
        # the queryset filters
        filters.SearchFilter,
        social_network_filters.StatusFilter
    )
    pagination_class = pagination.DefaultPagination
    search_fields = ["to_user__first_name", "to_user__last_name", "to_user__user__email"]

    def get_queryset(self):
        return social_network_models.FriendRequest.filter_instance(
            {"from_user__user__id": self.request.user.id}
        )

    def get(self, request, *args, **kwargs):
        """Get List of Friend Requests"""
        filtered_queryset = self.filter_queryset(queryset=self.get_queryset())
        serializer = social_network_serializer.FriendRequestListSerializer(self.paginate_queryset(filtered_queryset),
                                                                           many=True)
        return Response(self.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)

    def post(self, request):
        """Send Friend Request API view"""
        try:
            serializer = self.serializer_class(data=request.data, context={"user": request.user})
            if serializer.is_valid(raise_exception=False):
                serializer.save()

                return Response(constants.ApplicationMessages.REQUEST_SENT, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(constants.ApplicationMessages.REQUEST_N_SENT, status=status.HTTP_400_BAD_REQUEST)


class FriendRequestDetailsAPIView(generics.GenericAPIView):
    """Details of Friend Request"""

    serializer_class = social_network_serializer.FriendRequestSendSerializer
    permission_classes = (permissions.IsUser,)

    def get_queryset(self, request_id):
        return social_network_models.FriendRequest.get_instance(
            {"id": request_id}
        )

    def get(self, request, request_id=None, *args, **kwargs):
        """Get Details of Friend Requests"""
        serializer = social_network_serializer.FriendRequestListSerializer(self.get_queryset(request_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, request_id=None, *args, **kwargs):
        """Update Friend Request Status"""
        instance = social_network_models.FriendRequest.objects.get(id=request_id)
        serializer = self.serializer_class(
            instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(f'Friend Request {serializer.data.get("status")}', status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUserAPIView(generics.GenericAPIView):
    """Send Friend Request"""

    serializer_class = social_network_serializer.FriendRequestSendSerializer
    permission_classes = (permissions.IsUser,)
    filter_backends = (
        # the queryset filters
        filters.SearchFilter,
    )
    pagination_class = pagination.DefaultPagination
    search_fields = ["first_name", "last_name", "user__email"]

    def get_queryset(self):
        return social_network_models.Profile.filter_instance(
            {"is_active": True}
        )

    def get(self, request, *args, **kwargs):
        """Get List of active Users"""
        filtered_queryset = self.filter_queryset(queryset=self.get_queryset())
        serializer = social_network_serializer.UserListSerializer(self.paginate_queryset(filtered_queryset),
                                                                  many=True)
        return Response(self.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)
