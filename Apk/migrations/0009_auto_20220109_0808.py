# Generated by Django 3.2.7 on 2022-01-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0008_remove_customer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=1, max_length=155),
        ),
        migrations.AddField(
            model_name='customer',
            name='district',
            field=models.CharField(default=1, max_length=155),
        ),
    ]