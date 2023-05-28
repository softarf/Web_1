from django.db import models

# Create your models here.


#                                         7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
class Person(models.Model):
    # person_id = models.BigAutoField(primary_key=True)    # Можно задать свой первичный ключ.
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #
    objects = models.Manager()          # Диспетчер записей. Для PyCharm Community объявлять явно.
