# Generated by Django 4.1.1 on 2022-09-13 09:20

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
                ("username", models.CharField(max_length=30, unique=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                ("avatar", models.ImageField(blank=True, upload_to="images/users")),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
