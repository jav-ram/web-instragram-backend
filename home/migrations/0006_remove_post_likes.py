# Generated by Django 2.1.2 on 2018-10-08 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]