# Generated by Django 4.2.17 on 2025-01-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
    ]
