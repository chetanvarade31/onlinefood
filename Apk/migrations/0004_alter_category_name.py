# Generated by Django 3.2.7 on 2021-12-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
