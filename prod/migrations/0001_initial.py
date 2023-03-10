# Generated by Django 4.1.7 on 2023-03-02 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, unique=True, verbose_name='Категория')),
                ('description', models.CharField(max_length=500, verbose_name='Описние')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование продукта')),
                ('price', models.IntegerField(verbose_name='Цена продукта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('True', 'Активна'), ('False', 'Неактивна')], default='False', max_length=10, verbose_name='Признак публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prod.categories')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=250, verbose_name='Имя версии')),
                ('version_status', models.CharField(choices=[('active', 'активна'), ('inactive', 'неактивна')], default='inactive', max_length=10, verbose_name='Статус')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prod.product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
