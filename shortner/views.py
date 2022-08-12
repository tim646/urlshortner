from django.shortcuts import render
import uuid
from .models import Urls

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=url, uid=uid)
        new_url.save()
        return HttpResponse(uid)


def go_url_page(request, pk):
    try:
        data_page = Urls.objects.get(uid=pk)
        return HttpResponseRedirect(redirect_to=data_page.link)
    except:
        return HttpResponseNotFound('NOT FOUND')
