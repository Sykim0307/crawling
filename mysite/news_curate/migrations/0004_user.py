# Generated by Django 4.1.13 on 2024-01-14 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_curate', '0003_alter_article_read_time_alter_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('pwd', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.ImageField(upload_to='uploads')),
            ],
            options={
                'db_table': 'django_users',
            },
        ),
    ]