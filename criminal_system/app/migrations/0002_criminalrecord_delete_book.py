# Generated by Django 5.1.1 on 2024-09-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('nin', models.CharField(max_length=20)),
                ('crime_committed', models.TextField()),
                ('residence_before_arrest', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='criminal_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
