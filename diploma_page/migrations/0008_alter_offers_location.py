# Generated by Django 4.2.6 on 2023-12-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma_page', '0007_alter_offers_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
