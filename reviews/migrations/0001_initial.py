# Generated by Django 5.0 on 2024-02-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Заголовок"
                    ),
                ),
                (
                    "review",
                    models.TextField(
                        blank=True, max_length=100, null=True, verbose_name="Отзыв"
                    ),
                ),
                (
                    "date_start",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "data_end",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата закрытия"
                    ),
                ),
            ],
            options={
                "verbose_name": "Врач",
                "verbose_name_plural": "Врачи",
            },
        ),
    ]
