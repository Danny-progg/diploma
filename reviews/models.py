from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='Заголовок', **NULLABLE)
    review = models.TextField(max_length=100, verbose_name='Отзыв', **NULLABLE)
    date_start = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="Дата закрытия", **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Version(models.Model):
    objects = None
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name='Отзыв')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    version_sign = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.review}.'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        permissions = [
            ('change_version_sign', 'изменение признака текущей версии')
        ]