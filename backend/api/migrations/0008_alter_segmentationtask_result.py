# Generated by Django 4.1 on 2022-08-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_segmentationtask_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmentationtask',
            name='result',
            field=models.ForeignKey(help_text='Corresponding Task Result', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.resultdata'),
        ),
    ]
