# Generated by Django 4.1.6 on 2023-03-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='camper_image',
            field=models.URLField(default=''),
        ),
    ]
