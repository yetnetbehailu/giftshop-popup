# Generated by Django 3.2 on 2022-03-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220227_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_service',
            field=models.BooleanField(default=False),
        ),
    ]
