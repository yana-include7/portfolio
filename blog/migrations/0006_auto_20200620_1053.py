# Generated by Django 3.0.6 on 2020-06-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='text',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
