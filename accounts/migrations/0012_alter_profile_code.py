# Generated by Django 4.2.6 on 2024-04-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(default='3WA7TZYC', max_length=9),
        ),
    ]
