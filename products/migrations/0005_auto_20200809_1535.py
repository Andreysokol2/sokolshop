# Generated by Django 3.0.8 on 2020-08-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200809_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
