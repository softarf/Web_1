
from django import forms


#                                             6.1. Определение форм. Стр. 172 - 177.
#                                             6.2. Использование в формах POST-запросов. Стр. 177 - 179.
class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")
    # HTML: <input type="text">
    age = forms.IntegerField(label="Введите целое число", required=False)
    # HTML: <input type="number">


#                                             6.3. Использование полей в формах Django. Стр. 179 - 212.
class FormsList(forms.Form):
    basket = forms.BooleanField(label="Положить товар в корзину", required=False)
    # HTML: <input type="text">

    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
    # HTML:
    #     <select>
    #       <option value="1" selected="selected">Неизвестно</option>
    #       <option value="2">Да</option>
    #       <option value="3">Нет</option>
    #     </select>

    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")
    # HTML: <input type="text">

    email = forms.EmailField(label="Электроный адрес", help_text="Обязательный символ @", required=False)
    # HTML: <input type="email">

    ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text="Пример формата 192.0.2.0", required=False)
    # HTML: <input type="text">

    reg_text = forms.RegexField(label="Шаблон поиска", regex="^[0-9][A-F][0-9]$", required=False)
    # HTML: <input type="text">

    slug_text = forms.SlugField(label="Введите текст", required=False, allow_unicode=False)
    # HTML: <input type="text">

    url_text = forms.URLField(label="Введите URL", help_text="Например http://www.yandex.ru", required=False)
    # HTML: <input type="url">

    uuid_text = forms.UUIDField(label="Введите UUID",
                                help_text="Формат хххххххх-хххх-хххх-хххх-хххххххххххх", required=False)
    # HTML: <input type="text">

    combo_text = forms.ComboField(label="Введите URL",
                                  fields=[forms.URLField(), forms.CharField(max_length=20)], required=False)
    # HTML: <input type="text">

    file_path = forms.FilePathField(label="Выберите файл",
                                    path="E:/PyFiles/500__Python_Django_and_PyCharm/Web_1/hello",
                                    allow_files=True, allow_folders=True, required=False)
    # HTML:
    #     <select>
    #       <option value="folder/file1">folder/file1</option>
    #       <option value="folder/file2">folder/file2</option>
    #       <option value="folder/file3">folder/file3</option>
    #       // ...............................................
    #     </select>

    file = forms.FileField(label="Файл", allow_empty_file=True, required=False)
    # Генерируется объект 'UploadedFile'. Можно пустой файл.

    img_file = forms.ImageField(label="Изображение", required=False)
    # Генерируется объект 'UploadedFile'.

    date = forms.DateField(label="Введите дату", required=False)
    # HTML: <input type="text">

    time = forms.TimeField(label="Введите время", required=False)
    # HTML: <input type="text">

    date_time = forms.DateTimeField(label="Введите дату и время", required=False)
    # HTML: <input type="text">

    time_delta = forms.DurationField(label="Введите промежуток времени", required=False)
    # HTML: <input type="text">

    date_and_time = forms.SplitDateTimeField(label="Введите дату и время", required=False)
    # HTML:
    #     <input type="text" name="_0">
    #     <input type="text" name="_1">

    int_num = forms.IntegerField(label="Введите целое число", required=False)
    # HTML: <input type="number">

    dicimal_num = forms.DecimalField(label="Введите десятичное число",
                                     max_digits=5, decimal_places=2, required=False)
    # HTML: <input type="number">

    float_num = forms.FloatField(label="Введите число", required=False)
    # HTML: <input type="number">

    ling = forms.ChoiceField(label="Выберите язык",
                            choices=((1, "Английский"),
                                     (2, "Немецкий"),
                                     (3, "Французский")),
                            required=False)
    # HTML:
    #     <select>
    #       <option value="1">Data 1</option>
    #       <option value="2">Data 2</option>
    #       <option value="3">Data 3</option>
    #     </select>

    city = forms.TypedChoiceField(label="Выберите город",
                            empty_value=None,
                            choices=((1, "Москва"),
                                     (2, "Воронеж"),
                                     (3, "Курск")),
                            required=False)
    # HTML:
    #     <select>
    #       <option value="1">Data 1</option>
    #       <option value="2">Data 2</option>
    #       <option value="3">Data 3</option>
    #     </select>

    country = forms.MultipleChoiceField(label="Выберите страну",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Испания"),
                                                 (4, "Россия")),
                                        required=False)
    # HTML:
    #     <select>
    #       <option value="1">Data 1</option>
    #       <option value="2">Data 2</option>
    #       <option value="3">Data 3</option>
    #     </select>

    multi_city = forms.TypedMultipleChoiceField(label="Выберите страну",
                                                empty_value=None,
                                                choices=((1, "Москва"),
                                                         (2, "Воронеж"),
                                                         (3, "Курск"),
                                                         (4, "Томск")),
                                                required=False)
    # HTML:
    #     <select>
    #       <option value="1">Data 1</option>
    #       <option value="2">Data 2</option>
    #       <option value="3">Data 3</option>
    #     </select>


#                                             6.4. Настройка формы и её полей. Стр. 212 - 232.
#                                         6.4.1. Изменение внешнего вида поля с помощью параметра wiget. Стр. 212 - 213.
class WigetFieldForm(forms.Form):
    name = forms.CharField(label="Имя")
    # HTML: <input type="text">
    age = forms.IntegerField(label="Возраст", required=False)
    # HTML: <input type="number">
    comment1 = forms.CharField(label="Коментарий1", required=False)
    # HTML: <input type="text">
    comment2 = forms.CharField(label="Коментарий2", required=False,
                               widget=forms.Textarea)


#                                         6.4.2. Задание начальных значений полей с помощью свойства initial. Стр. 214.
class InitialFieldForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО")
    age = forms.IntegerField(label="Возраст", initial=18, required=False)
    comment = forms.CharField(label="Коментарий", widget=forms.Textarea, required=False)


# 1)                                      6.4.3. Задание порядка следования полей на форме. Стр. 214 - 216.
class OrderFieldForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО")
    age = forms.IntegerField(label="Возраст", initial=18, required=False)
    field_order = ["age", "name"]
# 2) Использую класс InitialFieldForm.


#                                         6.4.4. Задание подсказок к полям формы. Стр. 216 - 217.
class HelpFieldForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите ФИО")
    age = forms.IntegerField(label="Возраст", help_text="Введите возраст", required=False)


#                                         6.4.5. Настройки вида формы. Стр. 217 - 218.
class ViewForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="Возраст", required=False)


#                                         6.4.6. Проверка (валидация) данных. Стр. 218 - 223.
class ValidForm(forms.Form):
    name = forms.CharField(label="Имя", min_length=2, max_length=20)
    age = forms.IntegerField(label="Возраст", min_value=1, max_value=120, required=False)
    weight = forms.DecimalField(label="Вес", min_value=3, max_value=200, decimal_places=2, required=False)
    advertis = forms.BooleanField(label="Согласны получать рекламу", required=False)


#                                         6.4.7. Детальная настройка полей формы. Стр. 223 - 227.
class SetFieldsForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=2, max_length=20)
    age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=120)
