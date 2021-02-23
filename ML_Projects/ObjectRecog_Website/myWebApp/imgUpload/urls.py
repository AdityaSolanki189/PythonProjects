from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'image_process', views.image_process, name= 'image_process')
]
