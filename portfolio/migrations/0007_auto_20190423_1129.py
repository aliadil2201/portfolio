# Generated by Django 2.2 on 2019-04-23 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190423_1126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectFeatures',
            new_name='LatestProjectFeatures',
        ),
    ]