# Generated by Django 3.2.6 on 2021-08-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20210804_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
