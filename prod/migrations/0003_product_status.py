# Generated by Django 4.1.7 on 2023-02-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Активна'), ('False', 'Неактивна')], default='False', max_length=10, verbose_name='Признак публикации'),
        ),
    ]
