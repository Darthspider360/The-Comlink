# Generated by Django 4.2.17 on 2025-01-17 09:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_alter_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='file'),
        ),
    ]
