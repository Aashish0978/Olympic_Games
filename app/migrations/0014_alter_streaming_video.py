# Generated by Django 4.2.1 on 2023-06-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_streaming_video_url_streaming_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streaming',
            name='video',
            field=models.FileField(upload_to='app/assets/videos'),
        ),
    ]
