# Generated by Django 4.2.1 on 2023-06-13 14:57

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='blogsimage')),
                ('description', models.TextField(max_length=10000)),
                ('date', models.DateField(auto_now=True)),
                ('details_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title', unique=True)),
            ],
        ),
    ]
