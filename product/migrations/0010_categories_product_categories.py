# Generated by Django 4.2.6 on 2024-04-27 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='brand', verbose_name='Images')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_categories', to='product.categories', verbose_name='Categories'),
        ),
    ]
