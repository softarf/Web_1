from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# Create your views here.

def index(request):
    data = {
        "header": "Передача параметров в шаблон Django.",
        "message": "Загружен шаблон 'templates/firstapp/index_app1.html'."
    }
    return render(request, "firstapp/index_app1.html", context=data)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    # return HttpResponse("<h2>Контакты</h2>")
    #                                        Временная переадресация на страницу "О сайте".
    return HttpResponseRedirect('/about')  # Косая черта (/) обязательно должна стоять в начале пути.


def products(request, product_id=1):
    category = request.GET.get("cat", "")
    # output = f"<h2>Продукт № {product_id}</h2>"
    output = f"<h2>Продукт № {product_id} Категория: {category}</h2>"
    return HttpResponse(output)


def users(request):    # Убрали параметры представления - ", user_id=1, name='Андрей'".
    user_id = request.GET.get("user_id", 1)
    name = request.GET.get("name", "Андрей")
    output = f"<h2>Пользватель</h2><h3>id: {user_id} Имя: {name}</h3>"
    return HttpResponse(output)


def details(request):
    # return HttpResponse("<h2>Контакты</h2>")
    return HttpResponsePermanentRedirect('/')  # Постоянная переадресация на страницу "Главная".


def index_1(request):
    # return HttpResponse("<h2>Главная</h2>")
    # return render(request, "index.html")
    # return render(request, "firstapp/home.html")
    return TemplateResponse(request, "firstapp/home.html")
