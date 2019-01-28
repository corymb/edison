from operator import or_
from functools import reduce

from django.db.models import Q


class Search:
    """
    Thin wrapper over data layer.
    """
    def get_results(self, query, model):
        """
        Gets searchable fields from model, constructs a query to OR any 
        case-insensitive match for `query`.
        """
        if not query:
            return []
        else:
            # I don't like this much and I'm sure there's a better way but it'll do for our purposes:
            clauses = (Q(**{"%s__icontains" %field: query }) for field in model.SEARCHABLE_FIELDS)
            return model.objects.filter(reduce(or_, clauses))
