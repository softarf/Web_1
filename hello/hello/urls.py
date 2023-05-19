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
from django.views.generic import TemplateView

from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.index_hello),      # 3.4 Первое приложение на Django. Стр 102.
    #                                         4.1 Обработка запросов пользователей. Стр 106.
    path('first_request/', views.index_request),
    path('first_request/about/', views.about_request),
    path('first_request/contact/', views.contact_request),
    #                                        4.2 Маршрутизация запросов пользователя в функции re_path. Стр 110.
    path('re_pattr/', views.index_request),                # Распознавание адреса URL с помощью регулярного выражения.
    re_path(r'^re_pattr/about', views.about_request, name='about'),
    re_path(r'^re_pattr/contact', views.contact_request, name='contact'),
    #                                         4.5. Параметры представлений (задаются в строке URL).
    #                                         4.5.1. Определение параметров через функцию 're_path()'. Стр 114 - 117.
    re_path(r'^re_pattr/products/(?P<product_id>\d+)/', views.products_view_params),
    re_path(r'^re_pattr/products/$', views.products_view_params),    # По умолчанию.
    re_path(r'^re_pattr/users/(?P<user_id>\d+)/(?P<name>\D+)/', views.users_view_params),
    re_path(r'^re_pattr/users/$', views.users_view_params),          # По умолчанию.
    #                                         4.5.2. Определение параметров через функцию 'path()'. Стр 118 - 119.
    path('view_params/products/<int:product_id>/', views.products_view_params),
    path('view_params/products/', views.products_view_params),       # По умолчанию. 4.5.3... Стр 119 - 121.
    path('view_params/users/<int:user_id>/<name>/', views.users_view_params),
    path('view_params/users/', views.users_view_params),             # По умолчанию. 4.5.3... Стр 119 - 121.
    #                                         4.6. Параметры строки запроса пользователя. Стр 121 - 123.
    path('query_string/products/<int:product_id>/', views.products_query_string_params),
    path('query_string/products/', views.products_query_string_params),    # По умолчанию.
    path('query_string/users/', views.users_query_string_params),
    #                                         4.7.1. Переадресация. Стр 124 - 125.
    path('redirect/contact/', views.contact_redirect),
    path('redirect/details/', views.details_redirect),

    # path('', views.index_wth_base),
    path('about/', TemplateView.as_view(template_name='firstapp/about.html')),
    path('contact/', TemplateView.as_view(
            template_name='firstapp/contact.html',
            extra_context={"work": "Разработка программных продуктов."})
    ),
    path('index_old/', views.index_old),
    # path('with_base/', views.index_wth_base),
]
