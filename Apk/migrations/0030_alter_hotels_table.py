# Generated by Django 4.0.3 on 2022-04-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0029_table_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='table',
            field=models.PositiveIntegerField(),
        ),
    ]