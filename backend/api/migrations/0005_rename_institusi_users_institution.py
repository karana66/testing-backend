# Generated by Django 4.1 on 2022-08-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_segmentationdata_segmentationresult_segmentationtask_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='institusi',
            new_name='institution',
        ),
    ]