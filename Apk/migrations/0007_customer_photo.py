# Generated by Django 3.2.7 on 2022-01-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0006_auto_20220104_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
