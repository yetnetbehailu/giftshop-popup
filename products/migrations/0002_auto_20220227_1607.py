# Generated by Django 3.2 on 2022-02-27 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d[0-9]$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('oil_painting', 'Oil Painting'), ('impasto_painting', 'Impasto Painting'), ('line_art', 'Line Art')], default=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d[0-9]$')]),
        ),
    ]