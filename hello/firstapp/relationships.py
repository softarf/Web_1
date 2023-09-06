from django.http import HttpResponse

from firstapp.models import Person, Product, Company, Order, OrderPosition


#                             7.6. Организация связей между таблицами в модели данных. Стр. 256 - 269.
#                             7.6.1. Организация связей между таблицами "один-ко-многим". Стр. 256 - 262.
def manage_one_to_many(request):
    """ """
    """ Работа с таблицами, имеющими связь 'Один-ко-Многим'.
        Главная/родительская/первичная модель связана с зависимой/дочерней/вторичная/подчинённой.
    """
    # Перечень всех товаров, которые производит компания "Электрон"
    prods_1 = Product.objects.filter(company__title="Электрон")  # <class 'django.db.models.query.QuerySet'>
    # Здесь использован атрибут 'title' главной модели 'Company' для фильтрации объектов зависимой модели 'Product'.
    print(f'prods_1 = {prods_1}')

    # Перечень всех товаров, которые производит компания "Электрон" (Все товары компании "Электрон").
    prods_2 = Company.objects.get(title="Электрон").products.all()  # <class 'django.db.models.query.QuerySet'>
    # Здесь использовано свойство 'related_name' зависимой модели 'Product' для обращения к ней из главной модели Company.
    print(f'prods_2 = {prods_2}')

    """ QuerySet - это список из объектов модели ('Company' или 'Product')
        Его можно перебрать в цикле. Или обратиться к отдельному элементу по индексу. """

    # Свойство 'related_name' позволяет изменить направление связи и обратиться из главной модели к зависимой.
    """ Работа с таблицами, имеющими связь 'Один-ко-Многим'.
    """
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
    # Метод 'get' не подходит для выбора товара перед изменением! Только 'filter()' или 'all()'.
    >>> Product.objects.filter(name="Планшет ipad").update(name="Планшет Ipad")
    1
    #               б) Идентифицировать компанию можно как по объекту/записи '<Company: Электрон>',
    #                  так и по ключу 'company_id'.
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


#                             7.6.2. Организация связей между таблицами "многие-ко-многим". Стр. 262 - 266.
def manage_many_to_many(request):
    """ """
    """ Работа с таблицами, имеющими связь 'Многие-ко-Многим'.
        ВЕДОМАЯ модель связана с ВЕДУЩЕЙ (в которой объявлено поле внешнего ключа ManyToManyField).
        Ведомая модель с ведущей являются СВЯЗАННЫМИ.
        К двум связанным моделям (источникам) создаётся третья СВЯЗУЮЩАЯ (промежуточная/соединительная).
    """
    # Перечень всех товаров из "Заказ № 2"
    prods_1 = Product.objects.filter(orders__number=4)  # <class 'django.db.models.query.QuerySet'>
    print(f'prods_1 = {prods_1}')

    # Свойство 'related_name' позволяет изменить направление связи и обратиться из ведомой модели к ведущей.
    """ Работа с таблицами, имеющими связь 'Многие-ко-Многим'.
    """
    '''

    #               Запуск интерпретатора Python:
    > python manage.py shell
    >>> from firstapp.models import Person, Product, Company, Order, OrderPosition

    #               Удаление объекта:
    >>> Product.objects.get(name="Телефон Xiaomi").delete()    # - ... модели 'Product'
    (1, {'firstapp.Product': 1})
    >>> Person.objects.get(name="Сергей").delete()             # - ... модели 'Person'
    (2, {'firstapp.Order': 1, 'firstapp.Person': 1})           # - одновременно удалился его заказ (удалятся все заказы)
    >>> Order.objects.get(number=2).delete()                   # - ... модели 'Order'
    (1, {'firstapp.Order': 1})
    >>> Order.objects.filter(person__name="Виктор").delete()   # - Удаление всех заказов Виктора
    (8, {'firstapp.OrderPosition': 4, 'firstapp.Order': 4})

    #               Создание объекта ведущей модели 'Order' ("пустой заказ от Максима"):
    >>> ord1 = Order.objects.create(number=4, person=Person.objects.get(name="Андрей"))
    <Order: Заказ № 4>
    >>> ord3 = Order.objects.create(person=Person.objects.get(name="Максим"))
    <Order: Заказ № 7>
    
    #              Внесение первого продукта в заказ с указанием нужного количества (создание заказа).
    #              Т. е. создание нового заказа с привязкой к нему заданного продукта с указанным количеством:
    #       выбирает продукт
    >>> prod1 = Product.objects.get(name="Ноутбук ASUS")
    >>> prod2 = Product.objects.get(name="Ноутбук DELL")
    >>> prod3 = Product.objects.get(name="Телефон Samsung")
    >>> prod4 = Product.objects.get(name="Планшет Ipad")
    >>> prod5 = Product.objects.get(name="Телефон Iphone")
    >>> prod6 = Product.objects.get(name="Телефон Nokia")
    >>> prod7 = Product.objects.get(name="Планшет Samsung")
    >>> prod12 = Product.objects.get(name="Телефон Xiaomi")
    >>> prod13 = Product.objects.get(name="Ноутбук HP")
    #       создаёт новый заказ, присваивает пользователя, задаёт нужное количество продукта
    >>> ord2 = prod.orders.create(person=Person.objects.get(name="Виктор"), through_defaults={'quantity': 4})
    <Order: Заказ № 6>
    
    #              Внесение очередного продукта в заказ с указанием нужного количества (изменение заказа).
    #              Т. е. привязка к существующему заказу заданного продукта с указанным количеством:
    #       выбирает заказ
    >>> ord = Order.objects.get(number=5)
    #       выбирает продукт
    >>> prod = Product.objects.get(name="Ноутбук ASUS")
    >>> prod1 = Product.objects.get(name="Телефон Iphone")
    >>> prod2 = Product.objects.get(name="Телефон Nokia")
    >>> prod3 = Product.objects.get(name="Телефон Samsung")
    >>> prod4 = Product.objects.get(name="Планшет Samsung")
    
    #       1) создаёт связь при создании нового заказа с одновременным добавлением продукта
    >>> Order.objects.create(person=Person.objects.get(name="Максим")).products.add(prod5, through_defaults={'quantity': 2})
    
    #       2) а) создаёт связь, как добавление продукта к заказу
    >>> ord.products.add(prod, through_defaults={'quantity': 5})
    #       2) б) или, как добавление заказа к продукту
    >>> prod.orders.add(ord, through_defaults={'quantity': 5})    
    #       2) в) создаёт новую запись в промежуточной таблице
    >>> OrderPosition.orders.create(product=prod, order=ord, quantity=5)
    
    #       3) а) заменяет весь старый перечень продуктов на новый список (quantity устанавливается одинаковым)
    >>> Order.objects.get(number=7).products.set([prod3, prod4], clear=True, through_defaults={'quantity': 5})
    #       3) б) если clear=False, то если старого продукта нет в новом списке, то он удаляется,
    #          если есть, то он остаётся без изменений (quantity не меняется),
    #          продукт из нового списка, которого нет среди старых, добавляется (со своим новым quantity)
    >>> Order.objects.get(number=7).products.set([prod3, prod12], clear=False, through_defaults={'quantity': 3})
    
    #       4) создаёт связь, добавляя к заказу вновь создаваемый продукт
    >>> ord.products.create(name="Ноутбук HP", price=41000, company_id=2, through_defaults={'quantity': 3})
    1
    
    #              Удаление указанного продукта из заказа (изменение заказа).
    #              Т. е. удаление связи между указанным продуктом и заказом:
    #       выбирает заказ
    >>> ord = Order.objects.get(number=5)
    #       выбирает продукт
    >>> prod = Product.objects.get(name="Ноутбук ASUS")
    #       удаляет связи между заказом и указанными продуктами
    >>> ord.products.remove(prod1, prod3, ... , prod_N)
    #       удаляет связь продукта с заказом в одно действие
    >>> Order.objects.get(number=5).products.remove(Product.objects.get(name="Ноутбук ASUS"))
    #       или - заказа с продуктом:
    >>> Product.objects.get(name="Ноутбук ASUS").orders.remove(Order.objects.get(number=5))

    #               Демонстрация объектов ведомой модели 'Product', привязанных к указанному объекту ведущей
    #               модели 'Order':
    >>> Order.objects.get(number=4).products.all()
    <QuerySet [<Product: Телефон Xiaomi>, <Product: Телефон Iphone>]>

    #               Демонстрация объектов ведущей модели 'Order', привязанных к указанному объекту ведомой
    #               модели 'Product':
    >>> Order.objects.filter(products__name="Ноутбук ASUS")
    <QuerySet [<Order: Заказ № 2>, <Order: Заказ № 3>]>

    #               Количество всех заказов, в которых есть продукт "Ноутбук ASUS".
    >>> Product.objects.get(name="Ноутбук ASUS").orders.count()
    3
    >>>

    #                Так же доступны команды (для 'related_name').
    
    #   clear() - удаляет связи между всеми продуктами и указанным заказом.
    
    #   remove() - удаляет связи между указанными продуктами и указанным заказом.
    '''

    s = 'Заказы и их продукты:\r\n\r\n'
    for order in Order.objects.all():
        s += f'Заказ № {order.number}' + '\r\n'
        for position in order.positions.all():
            """ Все заказы перебираем по одному. Работаем через промежуточную таблицу 'order.positions.all()'.
                Через неё получаем доступ как к "Продуктам", так и к "Количеству".  Для выбранного заказа находим ссылку
                на таблицу "Продукты", переходим в неё. Выбираем в ней поле "Название" 'position.product.name'.
                В промежуточной таблице выбираем поле "Количество" 'position.quantity'.
            """
            s += '        ' + position.product.name + '  |  ' + str(position.quantity) + ' шт\r\n'
    content = s
    return HttpResponse(content, content_type='text/plain; charset=utf-8')    # "plain text" - Простой текст.


#                             7.6.3. Организация связей между таблицами "один-к-одному". Стр. 266 - 269.
def manage_one_to_one(request):
    """ """
    pass
    """ Работа с таблицами, имеющими связь 'Один-к-Одному'.
        ГЛАВНАЯ модель связана с ЗАВИСИМОЙ (в которой объявлено поле внешнего ключа OneToOneField).
        Главная модель и зависимая являются СВЯЗАННЫМИ.
    """
    """
                    1) С помощью связующего поля 'person' можно манипулировать объектами модели 'Person'.
        
    # Создадим пользователя Виктор
    viktor = Person.objects.create(name="Виктор", age=43)
    
    # Создадим аккаунт пользователя Виктор
    acc = Account.objects.create(login="viktor", password="1234", person=viktor)
    
    # Изменим имя пользователя
    acc.person.name = "Витя"
    acc.person.save()
    
                    2) С помощью диспетчера связи 'account' можно манипулировать объектами модели 'Account'.
        
    # Создадим пользователя Виктор
    viktor = Person.objects.create(name="Виктор", age=43)
    
    # Создадим аккаунт пользователя Виктор
    acc = Account(login="viktor", password="1234")
    viktor.account = acc
    viktor.account.save()
    
    # Изменим учётные данные пользователя
    viktor.account.login = "qwerty"
    viktor.account.password = "4321"
    viktor.account.save()
    """
