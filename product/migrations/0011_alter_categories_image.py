# Generated by Django 4.2.6 on 2024-04-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_categories_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='categories', verbose_name='Images'),
        ),
    ]
