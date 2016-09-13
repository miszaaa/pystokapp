from django.http import HttpResponse
from haystack.query import SearchQuerySet as SQS


def sample_view(request):
    return HttpResponse('Hello World')


def elastic_test(request):
    items = SQS().all()
    text = '<br>'.join([item.text for item in items])
    return HttpResponse(text)
