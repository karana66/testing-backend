# Generated by Django 4.1 on 2022-08-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='intuisi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
