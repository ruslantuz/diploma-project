# Generated by Django 4.2.6 on 2023-11-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma_page', '0002_alter_offers_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='offer_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]