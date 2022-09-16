# Generated by Django 4.1.1 on 2022-09-16 10:02

import blog.models.post
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="primary_image",
            field=models.ImageField(
                blank=True,
                upload_to=blog.models.post.get_path_to_store_post_primary_image,
            ),
        ),
        migrations.CreateModel(
            name="PostSecondaryImage",
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
                    "images",
                    models.FileField(
                        upload_to=blog.models.post.get_path_to_store_post_secondary_image
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
        ),
    ]
