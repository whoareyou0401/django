"""week01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from day04.views import *

urlpatterns = [
    url(r'^firstindex/', firstindex,name='firstindex'),
    url(r'^langs/', langs,name='langs'),
    url(r'^erindex/', erindex),
    url(r'^myindex_with_params/(\d+)$', myindex_with_params,name='myindex_with_params'),
    url(r'^myindex_with_params_v1/(?P<p1>\d+)$', myindex_with_params_v1, name='myindex_with_params_v1'),
    url(r'^new_reverse/', new_reverse),
    url(r'^extent/', extent),
]
