# Generated by Django 3.2.4 on 2021-07-18 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_color_productgallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.color'),
        ),
    ]
