# Generated by Django 4.2.17 on 2025-01-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_post_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]