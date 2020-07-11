from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import URLs
from urllib import parse as ps_url
import urllib
import hashlib
from .forms import *


def home(request):
    form = URLForm(request.GET) if request.method == "GET" else URLForm()
    if form.is_valid():
        pass
    return render(request, 'index.html', {'form': form})


def url_hashing(request):
    if request.method == 'GET':
        params = request.GET
        form = URLForm(request.GET)
        if form.is_valid():
            form_data = form.data.dict()
            url = form_data.get("target_url")
        params = {"utm_campaign": form_data.get('utm_campaign'),
                  "utm_medium": form_data.get("utm_medium"),\
                  "source": form_data.get("source")}
        if not params.get("utm_campaign"):
            params.pop("utm_campaign")
        if not params.get("source"):
            params.pop("source")
        if not params.get("utm_medium"):
            params.pop("utm_medium")
        url_parse = ps_url.urlparse(url)
        query = url_parse.query
        url_dict = dict(ps_url.parse_qsl(query))
        if params:
            url_dict.update(params)
        url_new_query = ps_url.urlencode(url_dict)
        url_parse = url_parse._replace(query=url_new_query)
        new_url = ps_url.urlunparse(url_parse)
        hashObject = hashlib.md5(new_url.encode('utf-8'))
        hashed_url = hashObject.hexdigest()[:8]
        try:
            check_if_url_already_exists = URLs.objects.get(
                hashed_url=hashed_url)
        except URLs.DoesNotExist:
            hashed_url_obj = URLs(hashed_url=hashed_url, target_url=new_url)
            hashed_url_obj.save()
        return render(request, 'index.html', {
            'hashed_url': hashed_url
        })

def retrieve_target_url(request, input_url):
    target = get_object_or_404(URLs, hashed_url=input_url)
    target_url = target.target_url
    if(target_url[:4] != 'http'):
        target_url = 'http://'+ target_url
    return redirect(target_url)

