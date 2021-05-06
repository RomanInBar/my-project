# Generated by Django 3.2.1 on 2021-05-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substance', models.CharField(max_length=10, verbose_name='Вещество')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_one', models.CharField(max_length=4, unique=True, verbose_name='Первый элемент')),
                ('element_two', models.CharField(max_length=4, unique=True, verbose_name='Второй элемент')),
                ('result', models.CharField(max_length=10, verbose_name='Результат')),
            ],
        ),
    ]
