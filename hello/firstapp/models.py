from django.db import models

from django.conf import settings


# Create your models here.


#                                 7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
class Person(models.Model):
    # id = ... (AutoField)
    # Можно задать свой первичный ключ:
    # person_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #
    # orders = ...                    (Диспетчер обратной связи - Order)
    # account = ...                   (Диспетчер обратной связи - Account)
    objects = models.Manager()  # Диспетчер записей. Для PyCharm Community объявлять явно.
    DoesNotExist = models.Manager  # Собственное исключение. Для PyCharm Community объявлять явно.

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['name', ]
        # unique_together = ('article', 'rubric')    # Можно задать уникальность для сочетания значений полей.

    def __str__(self):
        return self.name


#                                 7.2. Типы полей в модели данных Django. Стр. 238 - 241.
class FieldsTypes(models.Model):
    #                             Типы полей в Django и их объявления в PostgreSQL.
    package_data = models.BinaryField(verbose_name="Бинарные данные", null=True, blank=True)
    # "bytes NULL"

    basket = models.BooleanField(verbose_name="Положить товар в корзину", null=True, blank=True)
    # "boolean NULL"

    # Тип 'NullBooleanField'   -   Устарел и не поддерживается.

    date = models.DateField(verbose_name="Дата", null=True, blank=True)
    # "data NULL"

    time = models.TimeField(verbose_name="Время", null=True, blank=True)
    # "time NULL"

    date_time = models.DateTimeField(verbose_name="Полная дата", null=True, blank=True)
    # "timestamp NULL"

    time_delta = models.DurationField(verbose_name="Интервал времени", null=True, blank=True)
    # "interval NULL"

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    # "serial NOT NULL"

    small_int = models.SmallIntegerField(verbose_name="Маленькое целое")
    # "smallint NOT NULL"                                    #              -32768 < small_int < 32767

    pos_small = models.PositiveSmallIntegerField(verbose_name="Маленькое положительное")
    # 'smallint NOT NULL CHECK ("Значение" > 0)'             #                   0 < pos_small < 32767

    int_num = models.IntegerField(verbose_name="Целое число")
    # "integer NOT NULL"                                     #          -2147483648 < int_num < 2147483647

    pos_int = models.PositiveIntegerField(verbose_name="Положительное число")
    # 'integer NOT NULL CHECK ("Значение" > 0)'              #                    0 < pos_int < 2147483647

    big_int = models.BigIntegerField(verbose_name="Большое целое")
    # "bigint NOT NULL"                                      # -9223372036854775808 < big_int < 9223372036854775807

    dicimal_num = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Десятичное число")  # XXXX.ZZ
    # "numeric(X, Z) NOT NULL"

    float_num = models.FloatField(verbose_name="Вещественное число")
    # "double precision NOT NULL"

    name = models.CharField(max_length=50, verbose_name="Имя клиента")
    # "varchar(50) NOT NULL"

    description = models.TextField(verbose_name="Описание")
    # "text NOT NULL"

    email = models.EmailField(max_length=254, verbose_name="Электронный адрес")
    # "varchar(254) NOT NULL"

    file = models.FileField(max_length=100, verbose_name="Имя айла")
    # "varchar(100) NOT NULL"

    file_path = models.FilePathField(max_length=100, verbose_name="Путь до файла")
    # "varchar(100) NOT NULL"

    image_path = models.EmailField(max_length=100, verbose_name="Путь до картинки")
    # "varchar(100) NOT NULL"

    ip_adres = models.GenericIPAddressField(verbose_name="IP адрес")
    # "inet NOT NULL"

    slug_text = models.SlugField(max_length=50, verbose_name="Слаг")
    # "varchar(50) NOT NULL"

    url_text = models.SlugField(max_length=200, verbose_name="URL-адрес")
    # "varchar(200) NOT NULL"

    uuid_text = models.UUIDField(max_length=36, verbose_name="UUID-адрес")
    # "uuid NOT NULL"


#                                 7.6.1. Организация связей между таблицами "один-ко-многим". Стр. 256 - 262.
class Company(models.Model):
    # id = ...
    title = models.CharField(max_length=30, verbose_name='Название')
    #
    # products = ...               (Диспетчер обратной связи - Product)
    objects = models.Manager()  # Диспетчер записей.

    def __str__(self):
        return self.title


class Product(models.Model):
    # id = ... (AutoField)
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='products', verbose_name='Производитель')
    # related_name='products'. Здесь products - диспетчер обратной связи с моделью Company.
    #
    # orders = ...                (Диспетчер обратной связи - Order)
    # positions = ...             (Диспетчер обратной связи - OrderPosition)
    objects = models.Manager()  # Диспетчер записей.

    def __str__(self):
        return self.name


#                                 7.6.2. Организация связей между таблицами "многие-ко-многим". Стр. 262 - 266.
def number_default():
    """ Предлагает начальное значение для поля 'number' модели 'Order'.
    """
    if settings.FILL_IN:
        # Находит пропущенное значение и предлагает его.
        for i in range(1, 32000):
            try:
                num = Order.objects.get(number=i)
            except Order.DoesNotExist:
                return i
        else:
            raise ValueError("Таблица 'Order' заполнена полностью.")
    else:
        # Находит максимальное имеющееся значение и увеличивает его на единицу.
        cur_num = Order.objects.aggregate(max_num=models.Max('number'))
        return 1 + cur_num['max_num'] if cur_num['max_num'] else 1


class Order(models.Model):
    # id = ... (AutoField)
    number = models.PositiveIntegerField(default=number_default, unique=True, verbose_name='Номер')
    products = models.ManyToManyField(Product, through='OrderPosition', related_name='orders', verbose_name='Продукт')
    # related_name='orders'. Здесь orders - диспетчер обратной связи с моделью Product.
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='orders', verbose_name='Заказчик')
    # related_name='orders'. Здесь orders - диспетчер обратной связи с моделью Person.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    executed = models.BooleanField(default=False, verbose_name='Завершённый')
    #
    # positions = ...             (Диспетчер обратной связи - OrderPosition)
    objects = models.Manager()  # Диспетчер записей.
    DoesNotExist = models.Manager  # Собственное исключение. Для PyCharm Community объявлять явно.

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['number', ]
        # unique_together = ('number', 'created_at')    # Можно задать уникальность для сочетания значений полей.

    def __str__(self):
        return f'Заказ № {self.number}'


class OrderPosition(models.Model):  # Объект связки продуктов и заказов ("Многие-Ко-Многим").
    # id = ... (AutoField)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions', verbose_name='Продукт')
    # related_name='positions'. Здесь positions - диспетчер обратной связи с моделью Product.
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions', verbose_name='Заказ')
    # related_name='positions'. Здесь positions - диспетчер обратной связи с моделью Order.
    order_number = models.PositiveIntegerField(editable=False, verbose_name='Номер заказа')
    quantity = models.IntegerField(default=1, verbose_name='Количество')
    #
    # Для моделей 'positions', это такой же менеджер (диспетчер записей), как и 'objects'.
    objects = models.Manager()  # Диспетчер записей.

    def save(self, *args, **kwargs):
        # Сохраняет номер текущего заказа.
        self.order_number = self.order.number
        return super().save(*args, **kwargs)


#                             7.6.3. Организация связей между таблицами "один-к-одному". Стр. 266 - 269.
class Account(models.Model):
    # id не создаётся, его заменяет person_id (созданный из поля person).
    login = models.CharField(max_length=20, verbose_name='Логин')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    #
    objects = models.Manager()  # Диспетчер записей.
