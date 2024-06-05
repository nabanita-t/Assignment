from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.exceptions import NotFound


class LargePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
    max_page_size = 1000


class DefaultPagination(PageNumberPagination):
    """
    Default pagination class.
    in case of invalid page, empty list will be returned.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        """Checking NotFound exception"""
        try:
            return super(DefaultPagination, self).paginate_queryset(
                queryset, request, view=view
            )
        except NotFound:  # intercept NotFound exception
            return list()

    def get_paginated_response(self, data):
        """Avoid case when self does not have page properties for empty list"""
        if hasattr(self, "page") and self.page is not None:
            return super(DefaultPagination, self).get_paginated_response(data)
        else:
            return Response(
                OrderedDict(
                    [
                        ("count", None),
                        ("next", None),
                        ("previous", None),
                        ("results", data),
                    ]
                )
            )
