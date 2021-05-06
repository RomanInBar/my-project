from django.db import models

class Elements(models.Model):
    element_one = models.CharField(verbose_name='Первый элемент', max_length=4, unique=True)
    element_two = models.CharField(verbose_name='Второй элемент', max_length=4, unique=True)
    result = models.CharField(verbose_name='Результат', max_length=10)
    description = models.CharField(verbose_name='Описание', max_length=512, default='Описание отсутствует')


class Table(models.Model):
    element = models.CharField(verbose_name='элемент', max_length=3)
    name = models.CharField(verbose_name='название', max_length=50)
    row = models.PositiveIntegerField(verbose_name='строка', default=0)
 
