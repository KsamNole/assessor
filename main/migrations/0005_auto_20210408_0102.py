# Generated by Django 3.1.7 on 2021-04-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210408_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='firstName',
            field=models.CharField(max_length=25, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='main',
            name='lastName',
            field=models.CharField(max_length=25, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='main',
            name='middleName',
            field=models.CharField(max_length=25, verbose_name='Фамилия'),
        ),
    ]
