# Generated by Django 5.1.2 on 2024-11-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypost", "0004_blogpost_delete_board_delete_post_delete_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("slug", models.CharField(max_length=100)),
                ("body", models.TextField()),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
