# Generated by Django 3.0 on 2020-02-08 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Action',
            new_name='Actions',
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='Projects',
        ),
    ]