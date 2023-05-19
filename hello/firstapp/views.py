from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# Create your views here.

def index_hello(request):                        # 3.4 Первое приложение на Django. Стр 102.
    return HttpResponse("Hello world! Это мой первый проект на Django!")


def index_request(request):                      # 4.1 Обработка запросов пользователей. Стр 106.
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


def index(request):
    # return render(request, "firstapp/home.html")
    return render(request, "firstapp/index.html")


def index_old(request):
    # return render(request, "index.html")
    # return render(request, "firstapp/home.html")
    # return TemplateResponse(request, "firstapp/home.html")
    # data = {
    #     "header": "Передача параметров в шаблон Django.",
    #     "message": "Загружен шаблон 'templates/firstapp/index_app1.html'."
    # }
    # return render(request, "firstapp/index_app1.html", context=data)
    header = "Персональные данные"                     # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]    # список
    user = {"name": "Максим", "age": 30}               # словарь
    addr = ("Виноградная", 23, 45)                     # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    # return render(request, "index.html", context=data)
    return TemplateResponse(request, "index.html", context=data)


def index_wth_base(request):
    return render(request, "firstapp/index_wth_base.html")
