# Generated by Django 4.0.4 on 2022-05-07 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0035_alter_reviews_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='time',
            field=models.TimeField(default=datetime.timedelta),
        ),
    ]
