# Generated by Django 4.0.1 on 2022-02-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_homepost_post_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.ImageField(default='', upload_to='')),
                ('links', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
