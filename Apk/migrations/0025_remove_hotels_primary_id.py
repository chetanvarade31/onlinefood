# Generated by Django 4.0.3 on 2022-04-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0024_hotels_primary_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='primary_id',
        ),
    ]
