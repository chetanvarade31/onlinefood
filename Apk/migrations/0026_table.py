# Generated by Django 4.0.3 on 2022-04-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0025_remove_hotels_primary_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('persons', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('mobile', models.CharField(max_length=122)),
                ('hotel_name', models.CharField(max_length=122)),
            ],
        ),
    ]
