# Generated by Django 5.0.1 on 2024-02-11 11:50

import shopapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_order_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=shopapp.models.product_preview_directory_path),
        ),
    ]
