
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    # return HttpResponse("<h2>Контакты</h2>")
    return HttpResponseRedirect('/about')    # Временная переадресация на страницу "О сайте".
                                             # Косая черта (/) обязательно должна присутствовать в начале пути.

def products(request, product_id=1):
    category = request.GET.get("cat", "")
    output = f"<h2>Продукт № {product_id} Категория: {category}</h2>"
    # output = f"<h2>Продукт № {product_id}</h2>"
    return HttpResponse(output)

def users(request):              # Убрали параметры представления - ", user_id=1, name='Андрей'".
    user_id = request.GET.get("user_id", 1)
    name = request.GET.get("name", "Андрей")
    output = f"<h2>Пользватель</h2><h3>id: {user_id} Имя: {name}</h3>"
    # output = f"<h2>Пользватель</h2><h3>id: {user_id} Имя: {name}</h3>"
    return HttpResponse(output)

def details(request):
    # return HttpResponse("<h2>Контакты</h2>")
    return HttpResponsePermanentRedirect('/')    # Постоянная переадресация на страницу "Главная".
