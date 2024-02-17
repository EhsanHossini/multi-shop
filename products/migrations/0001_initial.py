# Generated by Django 5.0.1 on 2024-02-16 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
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
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("number", models.IntegerField(verbose_name="Number")),
                ("subject", models.CharField(max_length=100, verbose_name="subjects")),
                ("body", models.TextField(verbose_name="message")),
            ],
        ),
        migrations.CreateModel(
            name="Size",
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
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField()),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="products.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
                ("discount", models.SmallIntegerField()),
                ("image", models.ImageField(upload_to="image/")),
                (
                    "offer",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="offer"
                    ),
                ),
                (
                    "times",
                    models.DateTimeField(auto_now_add=True, verbose_name="times"),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="categories",
                        to="products.category",
                    ),
                ),
                (
                    "color",
                    models.ManyToManyField(
                        related_name="products", to="products.color"
                    ),
                ),
                (
                    "size",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="products",
                        to="products.size",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Information",
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
                ("text", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="information",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
