# Generated by Django 3.2.6 on 2021-08-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20210804_1005'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webshop.product'),
        ),
    ]
