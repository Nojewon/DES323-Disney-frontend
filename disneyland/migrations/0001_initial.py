# Generated by Django 4.1.13 on 2023-11-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="userInfo",
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
                ("userName", models.TextField()),
                ("name", models.TextField()),
                ("passWord", models.TextField()),
                ("confirmpass", models.TextField()),
                ("email", models.TextField()),
            ],
        ),
    ]
