# Generated by Django 4.2.6 on 2023-10-13 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_tage_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_product', to='product.product', verbose_name='Product'),
        ),
    ]
