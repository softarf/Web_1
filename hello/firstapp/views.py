from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse

from firstapp.forms import UserForm, FormsList, WigetFieldForm, InitialFieldForm, OrderFieldForm
from firstapp.forms import HelpFieldForm, ViewForm, ValidForm, SetFieldsForm, FieldStylesForm
from firstapp.models import Person


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


#                                             6.1. Определение форм. Стр. 172 - 177.
def index_form(request):
    userform = UserForm()
    return render(request, "firstapp/index_form.html", context={"form": userform})


#                                             6.2. Использование в формах POST-запросов. Стр. 177 - 179.
def index_out(request):
    if request.method == "POST":
        name = request.POST.get("name")       # получить значение поля Имя.
        age = request.POST.get("age")         # получить значение поля Возраст.
        output = f"<h2>Пользователь</h2><h3>Имя - {name}, Возраст - {age}</h3>"
        return HttpResponse(output)
    else:
        userform = UserForm()
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                             6.3. Использование полей в формах Django. Стр. 179 - 212. 232
def index_fields(request):
    userform = FormsList()
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                             6.4. Настройка формы и её полей. Стр. 212 - 232.
#                                         6.4.1. Изменение внешнего вида поля с помощью параметра wiget. Стр. 212 - 213.
def index_fields_wiget(request):
    userform = WigetFieldForm()
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                         6.4.2. Задание начальных значений полей с помощью свойства initial. Стр. 214.
def index_fields_initial(request):
    userform = InitialFieldForm()
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                         6.4.3. Задание порядка следования полей на форме. Стр. 214 - 216.
def index_fields_order_in_form(request):  # 1)
    userform = OrderFieldForm()
    return render(request, "firstapp/index_out.html", context={"form": userform})


def index_fields_order_in_view(request):  # 2)
    userform = InitialFieldForm(field_order = ["age", "name"])
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                         6.4.4. Задание подсказок к полям формы. Стр. 216 - 217.
def index_fields_help(request):
    userform = HelpFieldForm()
    return render(request, "firstapp/index_out.html", context={"form": userform})


#                                         6.4.5. Настройки вида формы. Стр. 217 - 218.
def index_set_view_form(request):
    userform = ViewForm()
    return render(request, "firstapp/index_view_form.html", context={"form": userform})


#                                         6.4.6. Проверка (валидация) данных. Стр. 218 - 223.
def index_valid(request):
    if request.method == "POST":
        userform = ValidForm(request.POST)
        if userform.is_valid():
            # name = request.POST.get("name")    # Так получал значение поля "Имя" РАНЬШЕ.
            name = userform.cleaned_data["name"]       # Получить значение поля "Имя".
            return HttpResponse(f"<h2>Имя введено корректно - {name}</h2>")
        else:
            return HttpResponse("<h2>Ошибка ввода данных</h2>")
    else:
        userform = ValidForm()
    return render(request, "firstapp/index_table.html", context={"form": userform})


#                                         6.4.7. Детальная настройка полей формы. Стр. 223 - 227.
def index_set_fields(request):
    userform = SetFieldsForm()
    if request.method == "POST":
        userform = SetFieldsForm(request.POST)
        if userform.is_valid():
            # name = request.POST.get("name")    # Так получал значение поля "Имя" РАНЬШЕ.
            name = userform.cleaned_data["name"]       # Получить значение поля "Имя".
            age = userform.cleaned_data["age"]         # Получить значение поля "Возраст".
            return HttpResponse(f"<h2>Данные введены корректно.</h2><h3>Имя - {name}, Возраст - {age}</h3>")
    return render(request, "firstapp/index_fields_attr.html", context={"form": userform})


#                                         6.4.8. Присвоение стилей полям формы. Стр. 227 - 232.
def index_fields_css(request):
    userform = FieldStylesForm()
    if request.method == "POST":
        userform = FieldStylesForm(request.POST)
        if userform.is_valid():
            # name = request.POST.get("name")    # Так получал значение поля "Имя" РАНЬШЕ.
            name = userform.cleaned_data["name"]       # Получить значение поля "Имя".
            age = userform.cleaned_data["age"]         # Получить значение поля "Возраст".
            return HttpResponse(f"<h2>Данные введены корректно.</h2><h3>Имя - {name}, Возраст - {age}</h3>")
    return render(request, "firstapp/index_fields_css.html", context={"form": userform})


#                                         7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
#                                              Поля для ввода имени и возраста создаются тегами <input>.
#                                         7.4. Пример работы с объектами модели данных:
#                                              Чтение и запись информации в БД. Стр. 246 - 250.
def index_read(request):
    people = Person.objects.all()
    return render(request, "firstapp/index_crud.html", context={"people": people})


def save_in_db(request):
    if request.method == "POST":
        client = Person()
        client.name = request.POST.get("name")       # Получает значение поля "Имя".
        client.age = request.POST.get("age")         # Получает значение поля "Возраст".
        client.save()
    return HttpResponseRedirect("/read")


#                                         7.5. Пример работы с объектами модели данных:
#                                              Редактирование и удаление информации из БД. Стр. 250 - 256.
def edit_in_db(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/read")
        else:
            return render(request, "firstapp/edit_db.html", context={"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден.</h2>")


def delete_in_db(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/read")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден.</h2>")

    # TODO: Повторить параграфы 6.4.6., 6.4.7., 6.4.8., 7.4. и 7.5.
