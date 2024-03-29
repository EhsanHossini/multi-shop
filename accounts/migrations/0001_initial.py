# Generated by Django 5.0.1 on 2024-02-16 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="ادرس ایمیل",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=12, unique=True, verbose_name="شماره تلفن"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False, verbose_name="ادمین")),
            ],
            options={
                "verbose_name": "کاربر",
                "verbose_name_plural": "کاربر ها",
            },
        ),
        migrations.CreateModel(
            name="Otp",
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
                ("token", models.CharField(max_length=200, null=True)),
                ("number", models.CharField(max_length=11, verbose_name="شماره")),
                ("code", models.SmallIntegerField(verbose_name="کد")),
                ("expiration_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "کدتاید",
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                ("fullname", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(max_length=12)),
                ("address", models.CharField(max_length=300)),
                ("postal_code", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "ادرس کاربرها",
            },
        ),
    ]
