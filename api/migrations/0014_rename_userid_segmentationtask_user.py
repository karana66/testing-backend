# Generated by Django 4.1 on 2022-09-05 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_imagelist_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segmentationtask',
            old_name='userid',
            new_name='user',
        ),
    ]