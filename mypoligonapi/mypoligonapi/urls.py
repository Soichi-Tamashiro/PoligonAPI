"""mypoligonapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from mypoligon.views import *

# from mypoligon import Create_polygon

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polygon/create/", Create_polygon.as_view()),
    path("polygon/find/", Find_polygon.as_view()),
    path("polygon/list/", List_polygon.as_view()),
    path("polygon/verify/", Verify_point.as_view()),
]
