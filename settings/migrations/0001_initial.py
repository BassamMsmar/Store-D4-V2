# Generated by Django 4.2.6 on 2023-10-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company')),
                ('subtitle', models.TextField(max_length=500)),
                ('facebool_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('android_app', models.URLField(blank=True, null=True)),
                ('ios_app', models.URLField(blank=True, null=True)),
                ('call_us', models.IntegerField(blank=True, null=True)),
                ('email_us', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
