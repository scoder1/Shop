# Generated by Django 4.0.1 on 2022-02-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepost',
            name='post_link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
