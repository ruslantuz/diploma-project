# Generated by Django 4.2.6 on 2024-04-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma_page', '0017_alter_orders_check_in_alter_orders_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='check_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]
