from django.shortcuts import render

from search.search import Search


def home(request):
    return render(request, template_name='home.html')


def search(request):
    query = request.GET.get('q')  # default to an empty string if q not present
    search = Search()
    results = search.get_results(query)
    return render(request, template_name='search.html', context={
                'query': query, 'results': results})
