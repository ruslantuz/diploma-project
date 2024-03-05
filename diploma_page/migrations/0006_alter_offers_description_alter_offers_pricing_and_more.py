# Generated by Django 4.2.6 on 2023-12-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma_page', '0005_rename_offer_image_destinations_dest_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='offers',
            name='pricing',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offers',
            name='rating',
            field=models.IntegerField(max_length=2),
        ),
    ]