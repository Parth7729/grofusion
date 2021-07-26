# Generated by Django 3.2.4 on 2021-07-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
