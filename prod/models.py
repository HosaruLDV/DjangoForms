from django.db import models

# Create your models here.

class Product(models.Model):
    STATUS_TRUE = 'True'
    STATUS_FALSE = 'False'
    STATUSES = (
        (STATUS_TRUE, 'Активна'),
        (STATUS_FALSE, 'Неактивна'),
    )
    name = models.CharField(max_length=250, verbose_name='Наименование продукта')
    price = models.IntegerField(verbose_name='Цена продукта')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=10, default=STATUS_FALSE, verbose_name='Признак публикации')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.description}'


class Version(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        (STATUS_ACTIVE, 'активна'),
        (STATUS_INACTIVE, 'неактивна'),
    )

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Имя версии')
    version_status = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=10, verbose_name='Статус')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'{self.version_number} {self.version_name} {self.version_status}'


class Categories(models.Model):

    category = models.CharField(max_length=150, verbose_name='Категория', unique=True)
    description = models.CharField(max_length=500, verbose_name='Описние')

    def __str__(self):
        return f'{self.category}'