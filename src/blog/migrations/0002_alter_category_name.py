# Generated by Django 4.1.1 on 2022-09-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]