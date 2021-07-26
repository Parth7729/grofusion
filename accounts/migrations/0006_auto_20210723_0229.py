# Generated by Django 3.2.4 on 2021-07-22 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_premium_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='premium_member',
        ),
        migrations.CreateModel(
            name='PremiumUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]