from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home')
]
