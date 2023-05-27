from django.db import models

# Create your models here.


#                                         7.1. Создание моделей и миграции базы данных. Стр. 233 - 238.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #
    objects = models.Manager()          # Диспетчер записей. Для PyCharm Community объявлять явно.
