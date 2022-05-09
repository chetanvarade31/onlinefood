# Generated by Django 4.0.4 on 2022-05-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apk', '0030_alter_hotels_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='zipcode',
            field=models.CharField(blank=True, default=0, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved'), ('Picked By Courier', 'Picked By Courier'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered')], default='Pending', max_length=155, null=True),
        ),
    ]
