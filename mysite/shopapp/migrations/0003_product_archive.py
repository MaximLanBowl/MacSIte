# Generated by Django 5.0.1 on 2024-01-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_create_at_product_discount_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
