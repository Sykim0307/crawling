# Generated by Django 4.1.13 on 2024-01-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_curate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=50),
        ),
    ]
