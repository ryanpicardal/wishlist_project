from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^home$', views.home),
    url(r'^addproduct$', views.addproduct),
    url(r'^create$', views.create),
    url(r'^items/(?P<id>\d+)$', views.show),
    url(r'^addtolist/(?P<id>\d+$)', views.addtolist),
    url(r'^removefromlist/(?P<id>\d+$)', views.removefromlist),
    url(r'^delete/(?P<id>\d+$)', views.delete)
]
