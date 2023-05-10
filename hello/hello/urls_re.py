"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path

from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^products/(?P<product_id>\d+)/', views.products, name='products'),
    re_path(r'^products/$', views.products, name='products'),
    re_path(r'^users/(?P<user_id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    re_path(r'^users/$', views.users, name='users'),
]
