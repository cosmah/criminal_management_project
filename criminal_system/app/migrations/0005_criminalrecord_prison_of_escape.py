# Generated by Django 5.1.1 on 2024-09-29 05:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_criminalrecord_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminalrecord',
            name='prison_of_escape',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
