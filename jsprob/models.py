from django.db import models

class DataKlass(models.Model):
    log = models.CharField('Логин', max_length=120)
    fik = models.CharField('ФИО Учителя', max_length=300, default='0')
    klass = models.CharField('Класс', max_length=100, default='0')
    fios = models.TextField('ФИО-ы Учеников', default=0)
    vyhods = models.CharField('Выходы к доске', max_length=300, default=0)
    balls = models.CharField('Баллы', max_length=300, default=0)
    res1 = models.IntegerField('РезЦел1', default=0)
    res2 = models.IntegerField('РезЦел2', default=0)
    res3 = models.IntegerField('РезЦел3', default=0)
    pole1 = models.CharField('Поле1', max_length=500, default='0')
    pole2 = models.CharField('Поле2', max_length=500, default='0')
    pole3 = models.CharField('Поле3', max_length=500, default='0')

    def __str__(self):
        return self.log  #return f'Тема: {self.temazad}'

    class Meta:
        verbose_name = 'Данные по классам'
        verbose_name_plural = 'Классы'
        ordering = ['id']


class Indexs(models.Model):
    log = models.CharField('Указатели', max_length=90)
    ips = models.CharField('IP Users', max_length=800, default='0')
    ipskol = models.CharField('Quantity IP', max_length=200, default='0')
    curdate = models.DateField('Сегодняшняя дата', default='2022-01-01')
    pole1 = models.CharField('Поле1', max_length=300, default='0')
    pole2 = models.CharField('Поле2', max_length=300, default='0')
    pole3 = models.CharField('Поле3', max_length=300, default='0')

    def __str__(self):
        return self.log  #return f'Тема: {self.temazad}'

    class Meta:
        verbose_name = 'Индексы и указатели'
        verbose_name_plural = 'Индексы и указатели'
        ordering = ['id']
