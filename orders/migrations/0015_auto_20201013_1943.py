# Generated by Django 3.1.1 on 2020-10-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20201013_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='nub',
            field=models.IntegerField(default=1),
        ),
    ]
