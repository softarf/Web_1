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
    #                                         5.1. Создание и использование шаблонов.
    path('index_simple/', views.index_simple),       # "Общий шаблон". Стр 128 - 134.
    path('home_simple/', views.home_simple),         # "Шаблон приложения". Стр 135 - 137.
    #                                         5.2. Класс TemplateResponse. Стр. 137 - 138.
    path('home_simple_class/', views.home_simple),         # "Шаблон приложения". Стр 135 - 137.
    #                                         5.3. Передача данных в шаблоны. Стр 138 - 140.
    path('index_data/', views.index_data),
    #                                         5.4. Передача в шаблон сложных данных. Стр 141 - 143.
    path('complex_data/', views.index_complex_data),
    #                                         5.5.1. Основы каскадных таблиц стилей. Стр 143 - 145.
    #                                         5.5.2. Использование статичных файлов... Стр 148 - 152.
    path('home_styles/', views.home_styles),
    #                                       5.5.3. Использование класса TemplateView для вызова шаблонов. Стр 154 - 158.
    path('templ_as_view/', views.index),
    path('templ_as_view/about/', TemplateView.as_view(template_name='firstapp/about_not_base.html')),
    path('templ_as_view/contact/', TemplateView.as_view(template_name='firstapp/contact_not_base.html')),
    path('templ_as_view/contact_with_data/', TemplateView.as_view(
            template_name='firstapp/contact_not_base.html',
            extra_context={"work": "Разработка программных продуктов."})),
    #                                5.5.5. Расширение шаблонов HTML-страниц на основе базового шаблона. Стр. 161 - 164.
    path('with_base/', views.index_with_base),
    path('with_base/about/', views.about_with_base),
    path('with_base/contact/', views.contact_with_base),
    #                                      5.6. Использование специальных тегов в шаблонах HTML-страниц. Стр. 164 - 171.
    path('special_tags/', views.special_tags),
    #                                         6.1. Определение форм. Стр. 172 - 177.
    path('index_form/', views.index_form),
    #                                         6.2. Использование в формах POST-запросов. Стр. 177 - 179.
    path('index_out/', views.index_out),
    #                                         6.3. Использование полей в формах Django. Стр. 179 - 212.
    path('index_fields/', views.index_fields),
    #                                     6.4.1. Изменение внешнего вида поля с помощью параметра wiget. Стр. 212 - 213.
    path('fields_wiget/', views.index_fields_wiget),
    #                                     6.4.2. Задание начальных значений полей с помощью свойства initial. Стр. 214.
    path('fields_initial/', views.index_fields_initial),
    #                                     6.4.3. Задание порядка следования полей на форме. Стр. 214 - 216.
    path('order_in_form/', views.index_fields_order_in_form),  # 1)
    path('order_in_view/', views.index_fields_order_in_view),  # 2)
    #                                     6.4.4. Задание подсказок к полям формы. Стр. 216 - 217.
    path('fields_help/', views.index_fields_help),
    #                                     6.4.5. Настройки вида формы. Стр. 217 - 218.
    path('view_form/', views.index_set_view_form),
    #                                     6.4.6. Проверка (валидация) данных. Стр. 218 - 223.
    path('valid/', views.index_valid),
    #                                     6.4.7. Детальная настройка полей формы. Стр. 223 - 227.
    path('set_fields/', views.index_set_fields),
    #                                     6.4.8. Присвоение стилей полям формы. Стр. 227 - 232.
    path('fields_css/', views.index_fields_css),     # 1)
    #                                     7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
    #                                     7.2. Типы полей в модели данных Django. Стр. 238 - 241.
    #                                     7.3. Манипуляция с данными в Django на основе CRUD. Стр. 241 - 246.
    #                     7.4. Пример работы с объектами модели данных: Чтение и запись информации в БД. Стр. 246 - 250.
    path('read/', views.index_read),
    path('read/create/', views.save_in_db),
    #          7.5. Пример работы с объектами модели данных: Редактирование и удаление информации из БД. Стр. 250 - 256.
    path('read/edit/<int:id>', views.edit_in_db),
    path('read/delete/<int:id>', views.delete_in_db),
]
