# Generated by Django 2.2.5 on 2020-07-06 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200704_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guest',
            new_name='guests',
        ),
    ]
