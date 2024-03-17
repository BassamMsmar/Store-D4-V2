# Generated by Django 4.2.6 on 2024-03-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='6MJBRWV6', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Processed', 'Processed'), ('Delivered', 'Delivered'), ('Recieved', 'Recieved')], default='Recieved', max_length=10),
        ),
    ]
