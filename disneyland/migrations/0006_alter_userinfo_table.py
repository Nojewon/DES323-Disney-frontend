# Generated by Django 4.1.13 on 2023-11-20 22:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("disneyland", "0005_delete_disneylandreview"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="userinfo",
            table="user",
        ),
    ]
