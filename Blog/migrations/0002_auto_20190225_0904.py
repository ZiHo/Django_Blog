# Generated by Django 2.1.7 on 2019-02-25 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
