# Generated by Django 4.1.1 on 2022-09-19 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="title",
            new_name="tag",
        ),
    ]
