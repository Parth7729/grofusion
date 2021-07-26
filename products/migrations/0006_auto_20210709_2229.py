# Generated by Django 3.2.4 on 2021-07-09 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210709_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.productsize'),
        ),
    ]
