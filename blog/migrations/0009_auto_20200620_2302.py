# Generated by Django 3.0.6 on 2020-06-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_photo_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='post',
            name='text_podrobnee',
            field=models.TextField(blank=True, default='-'),
        ),
    ]
