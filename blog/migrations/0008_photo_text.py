# Generated by Django 3.0.6 on 2020-06-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200620_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='text',
            field=models.TextField(default='Здесь я'),
        ),
    ]