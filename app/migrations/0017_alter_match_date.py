# Generated by Django 4.2.1 on 2023-06-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_streaming_video_streaming_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
