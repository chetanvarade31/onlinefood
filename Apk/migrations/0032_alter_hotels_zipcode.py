# Generated by Django 4.0.4 on 2022-05-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0031_hotels_zipcode_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='zipcode',
            field=models.CharField(default=0, max_length=8),
        ),
    ]