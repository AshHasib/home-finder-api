# Generated by Django 2.2.7 on 2020-01-29 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rentpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentpost',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
