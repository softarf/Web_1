from django.db import models

# Create your models here.


#                                 7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
class Person(models.Model):
    # Можно задать свой первичный ключ:
    # person_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #
    objects = models.Manager()          # Диспетчер записей. Для PyCharm Community объявлять явно.
    DoesNotExist = models.Manager       # Собственное исключение. Для PyCharm Community объявлять явно.


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

    dicimal_num = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Десятичное число")    # XXXX.ZZ
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
