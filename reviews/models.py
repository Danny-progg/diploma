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
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'