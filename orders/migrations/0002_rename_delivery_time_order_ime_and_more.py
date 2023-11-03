# Generated by Django 4.2.6 on 2023-11-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_time',
            new_name='ime',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='C4DG74KT', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Recieved', 'Recieved'), ('Processed', 'Processed')], default='Recieved', max_length=10),
        ),
    ]
