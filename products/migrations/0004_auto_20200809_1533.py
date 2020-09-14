# Generated by Django 3.0.8 on 2020-08-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
