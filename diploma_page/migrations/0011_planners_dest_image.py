# Generated by Django 4.2.6 on 2024-03-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma_page', '0010_planners'),
    ]

    operations = [
        migrations.AddField(
            model_name='planners',
            name='dest_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
