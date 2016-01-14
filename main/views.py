from django.shortcuts import render
from django.http.response import HttpResponse
from main.models import Good
from django.shortcuts import get_object_or_404

# Create your views here.


def good_list_view(request):
    result = []
    for i in Good.objects.all():
        result.append(i.name)
    return HttpResponse(str(result))


def good_detail_view(request, good_id):
    good = get_object_or_404(Good, id=good_id)
    return HttpResponse(good.name)
