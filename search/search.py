from operator import or_
from functools import reduce

from django.db.models import Q

from search.models import Line


class Search:
    """
    Thin wrapper over data layer.
    """
    def get_results(self, query):
        if not query:
            return []
        else:
            # I don't like this much and I'm sure there's a better way but it'll do for our purposes:
            clauses = (Q(**{"%s__icontains" %field: query }) for field in Line.SEARCHABLE_FIELDS)
            return Line.objects.filter(reduce(or_, clauses))
