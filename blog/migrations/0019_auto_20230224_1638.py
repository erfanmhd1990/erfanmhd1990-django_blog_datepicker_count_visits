# Generated by Django 3.0.8 on 2023-02-24 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20230224_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1),
        ),
    ]