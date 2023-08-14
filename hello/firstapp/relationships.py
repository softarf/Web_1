from django.http import HttpResponse

from firstapp.models import Person, Product, Company


#                                 7.6.1. Организация связей между таблицами "один-ко-многим". Стр. 256 - 262.
def manage_one_to_many(request):
    """ """
    """ Работа с таблицами, имеющими связь 'Один-ко-Многим'.
        Главная/родительская модель связана с зависимой/дочерней/подчинённой.
    """
    # Перечень всех товаров, которые производит компания "Электрон"
    prods_1 = Product.objects.filter(company__title="Электрон")  # <class 'django.db.models.query.QuerySet'>
    # Здесь использован атрибут 'title' главной модели 'Company' для фильтрации объектов зависимой модели 'Product'.
    print(f'prods_1 = {prods_1}')

    # Свойство 'related_name' позволяет изменить направление связи и обратиться из главной модели к зависимой.
    """ Работа с таблицами, имеющими связь 'Один-ко-Многим'.
    """

    # Перечень всех товаров, которые производит компания "Электрон" (Все товары компании "Электрон").
    prods_2 = Company.objects.get(title="Электрон").products.all()  # <class 'django.db.models.query.QuerySet'>
    # Здесь использовано свойство 'related_name' зависимой модели 'Product' для обращения к ней из главной модели Company.
    print(f'prods_2 = {prods_2}')
    """ QuerySet - это список из объектов модели ('Company' или 'Product')
        Его можно перебрать в цикле. Или обратиться к отдельному элементу по индексу. """
    '''

    #               Запуск интерпретатора Python:
    > python manage.py shell

    #               Создание объекта главной модели 'Company':
    >>> Company.objects.create(title="Электрон")
    <Company: Электрон>                         # Объект 'Company' с именем "Электрон"
    >>> Company.objects.create(title="Ракета")
    <Company: Ракета>                           # Объект 'Company' с именем "Ракета"

    #               а) Создание объекта зависимой модели 'Product' с привязкой к объекту главной моделе 'Company':
    >>> Company.objects.get(title="Электрон").products.create(name="Ноутбук ASUS", price=51000)
    <Product: Ноутбук ASUS>
    >>> Company.objects.get(title="Электрон").products.create(name="Ноутбук DELL", price=55000)
    <Product: Ноутбук DELL>
    >>> Company.objects.get(title="Электрон").products.create(name="Телефон Samsung", price=42000)
    <Product: Телефон Samsung>
    >>> Company.objects.get(title="Ракета").products.create(name="Планшет ipad", price=34200)
    <Product: Планшет ipad>
    >>> Company.objects.get(title="Ракета").products.create(name="Телефон Iphone", price=60000)
    <Product: Телефон Iphone>

    #               б)
    >>> Product.objects.create(name="Телефон Nokia", price=29000, company_id=1)
    <Product: Телефон Nokia>

    #               а) Демонстрация объектов зависимой модели 'Product', привязанных к указанному объекту главной
    #                  модели 'Company':
    >>> Company.objects.get(title="Электрон").products.all()
    <QuerySet [<Product: Ноутбук ASUS>, <Product: Ноутбук DELL>, <Product: Телефон Samsung>]>
    >>> Product.objects.filter(company__title="Электрон")
    <QuerySet [<Product: Ноутбук ASUS>, <Product: Ноутбук DELL>, <Product: Телефон Samsung>]>

    #               б)
    >>> Company.objects.filter(id=1) 
    <QuerySet [<Company: Электрон>]>    # Объект класса 'QuerySet'.
    >>> Company.objects.get(id=1)
    <Company: Электрон>                 # Объект класса 'Company'.

    #               Типы, возвращаемые методами:
    >>> type(Company.objects.all())
    <class 'django.db.models.query.QuerySet'>
    >>> type(Company.objects.filter())
    <class 'django.db.models.query.QuerySet'>
    >>> type(Company.objects.get(title="Электрон"))
    <class 'firstapp.models.Company'>

    #               а) Демонстрация объекта главной модели 'Company', привязанного к указанному объекту зависимой
    #                  модели 'Product'.'
    >>> Product.objects.get(id=1).company
    <Company: Электрон>
    >>> Product.objects.get(id=1).company.title
    'Электрон'

    #               б)
    >>> Company.objects.filter(products__id=1)[0].title
    'Электрон'

    #               Количество всех товаров компании "Электрон".
    >>> Company.objects.get(title="Электрон").products.count()
    3

    #               а) Все товары, название которых начинается на "Ноутбук". (двойное подчёркивание)
    >>> Product.objects.filter(name__startswith="Ноутбук")
    <QuerySet [<Product: Ноутбук ASUS>, <Product: Ноутбук DELL>]>
    #               б) Все товары, название которых начинается на "Телефон". (двойное подчёркивание)
    >>> Product.objects.filter(name__startswith="Телефон") 
    <QuerySet [<Product: Телефон Samsung>, <Product: Телефон Iphone>, <Product: Телефон Nokia>]>

    #               а) Обновление товара.
    # Метод 'get' не подходит для выбора товара перед изменением! Только 'filter' или 'all'.
    >>> Product.objects.filter(name="Планшет ipad").update(name="Планшет Ipad")
    1
    #               б)
    >>> Product.objects.filter(name="Телефон Nokia").update(company=Company.objects.get(title="Ракета"))
    1
    >>> Product.objects.filter(name="Телефон Nokia").update(company_id=2)       # "Ракета"
    1
    >>> Product.objects.filter(name="Телефон Nokia").update(company_id=Company.objects.get(title="Электрон").id)
    1

    #                                     Также есть команды для 'related_name'.
    
    #   add() - заносит новый товар в БД и добавляет связь его с компанией.
    >>> prod = Product(name="Планшет Samsung", price=31000)
    >>> Company.objects.get(title="Электрон").products.add(prod, bulk=False)       # или "Ракета"
    #   bulk=False - обязательно, т.к. в момент установления связи 'prod' ещё не занесён в базу.
    
    #   clear() - удаляет все связи между всеми товарами и указанной компанией.
    >>> Company.objects.get(title="Электрон").products.clear()
    #   при этом сами товары не удаляются, остаются в базе.
    #   Обязательно в зависимой моделе поле ForeignKey(Company, null=True)
    
    #   remove() - удаляет связь между указанным товаром и указанной компанией.
    >>> Company.objects.get(title="Электрон").products.remove(prod)
    #   также, как и в случае с 'clear()', товар остаётся в базе.
    #   Обязательно в зависимой моделе поле ForeignKey(Company, null=True)
    '''

    s = 'Список компаний\r\n\r\n'
    for cc in Company.objects.all():
        s += cc.title + '\r\n'
    s += '\r\n\r\nСписок продуктов\r\n\r\n'
    for pp in Product.objects.all():
        s += pp.name + '\r\n'
    content = s
    return HttpResponse(content, content_type='text/plain; charset=utf-8')    # "plain text" - Простой текст.
