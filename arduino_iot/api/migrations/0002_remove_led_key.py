# Generated by Django 3.2.20 on 2024-07-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='led',
            name='key',
        ),
    ]
