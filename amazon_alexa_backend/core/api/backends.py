from .utils import query_params_to_filters
from rest_framework import filters

"""
Any filter containing any of the following is not allowed
"""
DISALLOWED_FILTERS = (
    'password',
)


class AAFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        query_params = {}

        if getattr(view, 'filter_class', None):
            for key, val in request.query_params.dict().items():
                """
                Check for the fields attribute of the filter class and
                include only the filters that are explicitly allowed
                """
                if getattr(view.filter_class._meta, 'fields', None):
                    for field_name in view.filter_class._meta.fields:
                        if key.startswith(field_name):
                            query_params[key] = val

                """
                Check for the excludes attribute of the filter class and
                sift out any filters that are explicitly forbidden
                """
                if getattr(view.filter_class._meta, 'exclude', None):
                    for field_name in view.filter_class._meta.exclude:
                        if key.startswith(field_name):
                            try:
                                del(query_params[key])
                            except KeyError:
                                pass

                """
                Remove any filters containing strings in DISALLOWED_FILTERS
                list.
                """
                for disallowed in DISALLOWED_FILTERS:
                    try:
                        if key.index(disallowed) >= 0:
                            try:
                                del(query_params[key])
                            except KeyError:
                                pass
                    except ValueError:
                        pass

            return queryset.filter(**query_params_to_filters(query_params))
        else:
            """
            If no filter_class is specified, ignore all
            """
            return queryset
