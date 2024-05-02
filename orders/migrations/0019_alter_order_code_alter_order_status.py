# Generated by Django 4.2.6 on 2024-05-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='T43ONVLM', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('Shipped', 'Shipped'), ('Processed', 'Processed'), ('Delivered', 'Delivered')], default='Recieved', max_length=10),
        ),
    ]
