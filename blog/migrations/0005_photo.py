# Generated by Django 3.0.6 on 2020-06-16 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200615_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='img/9.png', upload_to='img')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Post')),
            ],
        ),
    ]
