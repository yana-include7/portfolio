# Generated by Django 3.0.6 on 2020-06-20 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_photo_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile_image',
        ),
    ]