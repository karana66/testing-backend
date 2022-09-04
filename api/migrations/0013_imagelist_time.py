# Generated by Django 4.1 on 2022-09-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_imagelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelist',
            name='time',
            field=models.CharField(blank=True, help_text='Time of the image list was processed', max_length=50, null=True, verbose_name='time'),
        ),
    ]
