from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# Create your views here.

def index_hello(request):                   # 3.4 Первое приложение на Django. Стр 102.
    return HttpResponse("Hello world! Это мой первый проект на Django!")


def index_request(request):                 # 4.1 Обработка запросов пользователей. Стр 106.
    return HttpResponse("<h2>Главная</h2>")


def about_request(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact_request(request):
    return HttpResponse("<h2>Контакты</h2>")


#                                             4.5. Параметры представлений (задаются в строке URL). стр 114 - 121.
def products_view_params(request, product_id=1):
    output = f"<h2>Продукт № {product_id}</h2>"
    return HttpResponse(output)


def users_view_params(request, user_id=1, name='Андрей'):
    output = f"<h2>Пользватель</h2><h3>id: {user_id} Имя: {name}</h3>"
    return HttpResponse(output)


#                                             4.6. Параметры строки запроса пользователя. стр 121 - 123.
def products_query_string_params(request, product_id=1):
    category = request.GET.get("cat", "")          # Добавили параметр строки запроса (?cat=Cata).
    output = f"<h2>Продукт № {product_id} Категория: {category}</h2>"
    return HttpResponse(output)


def users_query_string_params(request):            # Убрали параметры представления.
    user_id = request.GET.get("user_id", 1)        # Добавили параметры строки запроса (?user_id=3&name=Виктор).
    name = request.GET.get("name", "Андрей")
    output = f"<h2>Пользватель</h2><h3>id: {user_id} Имя: {name}</h3>"
    return HttpResponse(output)


def contact_redirect(request):              # 4.7.1. Переадресация. Стр 124 - 125.
    #                                                         Временная переадресация на страницу "О сайте".
    return HttpResponseRedirect('/first_request/about')     # Косая черта (/) обязательно должна стоять в начале пути.


def details_redirect(request):
    return HttpResponsePermanentRedirect('/first_request')  # Постоянная переадресация на страницу "Главная".


def index_simple(request):                  # 5.1. Создание и использование шаблонов.
    return render(request, "index_simple.html")       # "Общий шаблон". Стр 128 - 134.


def home_simple(request):                            # "Шаблон приложения". Стр 135 - 137.
    return render(request, "firstapp/home_simple.html")


#                                             5.2. Класс TemplateResponse. Стр. 137 - 138.
def home_simple_class_template(request):    # Отображение шаблона классом 'TemplateResponse'.
    return TemplateResponse(request, "firstapp/home_simple.html")


def index_data(request):                    # 5.3. Передача данных в шаблоны. Стр 138 - 140.
    data = {
        "header": "Передача параметров в шаблон Django.",
        "message": "Загружен шаблон 'templates/firstapp/index_data.html'."
    }
    return render(request, "firstapp/index_data.html", context=data)


def index_complex_data(request):            # 5.4. Передача в шаблон сложных данных. Стр 141 - 143.
    header = "Персональные данные (через класс)"                     # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]    # список
    user = {"name": "Максим", "age": 30}               # словарь
    addr = ("Виноградная", 23, 45)                     # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    # return render(request, "index_complex_data.html", context=data)            # Через функцию 'render()'.
    return TemplateResponse(request, "index_complex_data.html", context=data)    # Через класс 'TemplateResponse'.


#                                             5.5.1. Основы каскадных таблиц стилей. Стр 143 - 145.
#                                             5.5.2. Использование статичных файлов... Стр 148 - 152.
def home_styles(request):    # Отображение шаблона классом 'TemplateResponse'.
    return TemplateResponse(request, "firstapp/home_styles.html")


#                                           5.5.3. Использование класса TemplateView для вызова шаблонов. Стр 154 - 158.
#   view-функция не требуется. Ответ формируется прямо в диспетчере URL-адресов.
def index(request):
    return render(request, "firstapp/home_styles.html")


#                                    5.5.5. Расширение шаблонов HTML-страниц на основе базового шаблона. Стр. 161 - 164.
def index_with_base(request):
    return render(request, "firstapp/index_with_base.html")


def about_with_base(request):
    return render(request, "firstapp/about_with_base.html")


def contact_with_base(request):
    return render(request, "firstapp/contact_with_base.html")


#                                          5.6. Использование специальных тегов в шаблонах HTML-страниц. Стр. 164 - 171.
def special_tags(request):
    data = {
        "age": 56,
        "cats": ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"],
    }
    return render(request, "firstapp/special_tags.html", context=data)
