# Generated by Django 3.2.10 on 2023-01-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataKlass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=120, verbose_name='Логин')),
                ('fik', models.CharField(default='0', max_length=300, verbose_name='ФИО Учителя')),
                ('klass', models.CharField(default='0', max_length=100, verbose_name='Класс')),
                ('fios', models.TextField(default=0, verbose_name='ФИО-ы Учеников')),
                ('vyhods', models.CharField(default=0, max_length=300, verbose_name='Выходы к доске')),
                ('balls', models.CharField(default=0, max_length=300, verbose_name='Баллы')),
                ('res1', models.IntegerField(default=0, verbose_name='РезЦел1')),
                ('res2', models.IntegerField(default=0, verbose_name='РезЦел2')),
                ('res3', models.IntegerField(default=0, verbose_name='РезЦел3')),
                ('pole1', models.CharField(default='0', max_length=500, verbose_name='Поле1')),
                ('pole2', models.CharField(default='0', max_length=500, verbose_name='Поле2')),
                ('pole3', models.CharField(default='0', max_length=500, verbose_name='Поле3')),
            ],
            options={
                'verbose_name': 'Данные по классам',
                'verbose_name_plural': 'Классы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Indexs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=90, verbose_name='Указатели')),
                ('ips', models.CharField(default='0', max_length=800, verbose_name='IP Users')),
                ('ipskol', models.CharField(default='0', max_length=200, verbose_name='Quantity IP')),
                ('curdate', models.DateField(default='2022-01-01', verbose_name='Сегодняшняя дата')),
                ('pole1', models.CharField(default='0', max_length=300, verbose_name='Поле1')),
                ('pole2', models.CharField(default='0', max_length=300, verbose_name='Поле2')),
                ('pole3', models.CharField(default='0', max_length=300, verbose_name='Поле3')),
            ],
            options={
                'verbose_name': 'Индексы и указатели',
                'verbose_name_plural': 'Индексы и указатели',
                'ordering': ['id'],
            },
        ),
    ]