# Utilities
def query_params_to_filters(query_params={}):
    """
    Convert query parameter values to appropriate type
    based on the filter clause included in the key
    """
    filters = {}
    for key, val in query_params.items():
        if key.find('__in') >= 0 or key.find('__range') >= 0:
            filters[key] = [
                member.strip() for member in val.split(',')
            ]
        else:
            filters[key] = val
    return filters
