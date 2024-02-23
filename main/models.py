from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Doctors(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    price = models.IntegerField(verbose_name="Цена", **NULLABLE)
    date_start = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="Дата закрытия", **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Version(models.Model):
    objects = None
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    version_sign = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.doctor}.'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        permissions = [
            ('change_version_sign', 'изменение признака текущей версии')
        ]