# Generated by Django 5.0 on 2024-02-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_service_doctors_alter_doctors_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
    ]
