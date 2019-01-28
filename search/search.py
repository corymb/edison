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
            return Line.objects.all()
