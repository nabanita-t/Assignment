from rest_framework.filters import BaseFilterBackend


class StatusFilter(BaseFilterBackend):
    """
    Filter the friend requests on basis of status filter
    """

    param = "status"

    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get(self.param, None)
        if status:
            return queryset.filter(status=status)
        return queryset
