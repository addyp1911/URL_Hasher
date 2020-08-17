from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .models import URLs
from urllib import parse as ps_url
import urllib
import hashlib
from .forms import *
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from django.contrib import messages
from .utils import *

def home(request):
    form = URLForm(request.GET) if request.method == "GET" else URLForm()
    search_form = SearchForm(request.GET) if request.method == "GET" else SearchForm()
    return render(request, 'index.html', {'form': form, "search_form": search_form})


def url_hashing(request):
    try:
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
                hashObject = hashlib.sha256(new_url.encode('utf-8'))
                hashed_url = hashObject.hexdigest()[:8]
                try:
                    response_url = URLs.objects.get(
                        hashed_url=hashed_url)
                except URLs.DoesNotExist:
                    hashed_url_obj = URLs(hashed_url=hashed_url, target_url=new_url)
                    response_url = hashed_url_obj.save()
                total_url_hits = response_url.total_url_hits
                return render(request, 'index.html', {
                    'hashed_url': hashed_url, "total_url_hits":total_url_hits
                })
            else:
                messages.warning(request, "Something went wrong!")   
    except AssertionError as ex:
        messages.warning(request, str(ex))   
    return render(request, 'index.html', {'form': form})     


def retrieve_target_url(request, input_url):
    from django.db.models import F
    target = get_object_or_404(URLs, hashed_url=input_url)
    target_url = target.target_url
    URLs.objects.filter(pk=target.pk).update(total_url_hits=F('total_url_hits')+1)
    if(target_url[:4] != 'http'):
        target_url = 'http://'+ target_url
    return redirect(target_url)


def search(request):
    if request.method == "GET":
        search_form = SearchForm(request.GET) if request.method == "GET" else SearchForm()
        return render(request, 'search_pages.html', {"search_form": search_form})

    elif request.method == "POST":
        form = SearchForm(request.POST)
        try:
            if form.is_valid():
                form_data = form.data.dict()
                url = form_data.get("search_url")
                search_params = form_data.get("search_keyword")
                response_data = requests.get(url)
                page = BeautifulSoup(response_data.content, features="html.parser")
                matched_links = lambda tag: (getattr(tag, 'name', None) == 'a' and
                                'href' in tag.attrs and
                                search_params in tag.get_text().lower())
                results = page.find_all(matched_links)
                result_links = [urljoin(url, tag['href']) for tag in results]
                pagenumber = request.GET.get('page', 1)
                paginator = Paginator(result_links, 10)
                res_data = list(paginator.page(pagenumber).object_list)
                links = paginate(res_data, paginator, pagenumber)
                return render(request,  'pages_list.html', {'links': links})
            else:
                form = SearchForm()
        except AssertionError as ex:
            messages.warning(request, str(ex))
        except Exception as ex:
            messages.warning(request, "Something went wrong!")
        return render(request, 'search_pages.html', {'form': form})     
         
