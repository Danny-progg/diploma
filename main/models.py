from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    price = models.IntegerField(verbose_name="Цена", **NULLABLE)
    date_start = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="Дата закрытия", **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'