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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'day01/',include('day01.urls',namespace='day01')),
    url(r'day02/', include('day02.urls',namespace='day02')),
    url(r'homework/', include('homework.urls',namespace='homework')),
    url(r'^day03/',include('day03.urls',namespace='day03')),
    url(r'^day04/', include('day04.urls',namespace='day04')),
    url(r'^day05/', include('day05.urls',namespace='day05')),
    url(r'^day06/',include('day06.urls',namespace='day06')),
]
