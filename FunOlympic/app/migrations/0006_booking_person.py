# Generated by Django 4.2.1 on 2023-06-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_blogs_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
