# Generated by Django 2.2.7 on 2019-12-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191205_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_img',
        ),
    ]
