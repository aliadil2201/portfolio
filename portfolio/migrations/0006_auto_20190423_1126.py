# Generated by Django 2.2 on 2019-04-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_contentformaddressinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='MyOfferedServices',
        ),
    ]