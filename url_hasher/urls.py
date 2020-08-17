"""url_hasher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from urlapp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', csrf_exempt(views.home), name="home"),
    url(r'^get_hashed_url/$', csrf_exempt(views.url_hashing), name="get_hashed_url"),
    url(r'^(?P<input_url>[0-9a-zA-Z]+)/$', csrf_exempt(views.retrieve_target_url), name="retrieve_url"),
    url(r'^search-keyword/$', csrf_exempt(views.search), name="search-pages"),

]
