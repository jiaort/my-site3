# -*- coding: utf-8 -*-

from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^blog-list/?$', views.blog_list),
    re_path(r'^get-banners/?$', views.get_banners),
]
