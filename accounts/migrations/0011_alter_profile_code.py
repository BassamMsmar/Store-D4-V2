# Generated by Django 4.2.6 on 2024-04-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(default='Q5VK3WG7', max_length=9),
        ),
    ]
