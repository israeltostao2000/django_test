# Generated by Django 3.2.20 on 2024-07-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_led_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(verbose_name='Led key')),
                ('led_status', models.IntegerField(verbose_name='Led Status')),
                ('time', models.IntegerField(verbose_name='Led Status')),
            ],
            options={
                'verbose_name_plural': 'Simulation',
            },
        ),
    ]