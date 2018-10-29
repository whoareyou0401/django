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

from homework.views import *

urlpatterns = [
    url(r'^addClass/', addClass),
    url(r'^addStudent/', addStudent),
    url(r'^get_stu_by_cla/', get_stu_by_cla),
    url(r'^get_cla_by_stu/', get_cla_by_stu),
    url(r'^play/', play),

]
