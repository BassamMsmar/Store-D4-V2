# Generated by Django 4.2.6 on 2024-04-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='sublogo',
            field=models.ImageField(blank=True, null=True, upload_to='company'),
        ),
    ]