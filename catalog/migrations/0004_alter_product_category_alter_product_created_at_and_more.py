# Generated by Django 5.1.1 on 2024-10-01 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="Выберете категорию",
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание...",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                help_text="Введите название...",
                max_length=150,
                verbose_name="Продукт (Вещь?)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(
                blank=True, help_text="Укажите цену", null=True, verbose_name="Цена"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата последнего изменения"
            ),
        ),
        migrations.CreateModel(
            name="Version",
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
                    "version_number",
                    models.PositiveIntegerField(
                        help_text="Введите описание...", verbose_name="Описание"
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        help_text="Введите название версии...",
                        max_length=300,
                        verbose_name="Название версии",
                    ),
                ),
                ("current_version", models.BooleanField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]