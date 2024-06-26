# Generated by Django 5.0.3 on 2024-05-22 09:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='card_holder',
            field=models.CharField(default='unknown name', max_length=200),
        ),
        migrations.AddField(
            model_name='account',
            name='cvv',
            field=models.IntegerField(default='123'),
        ),
        migrations.AddField(
            model_name='account',
            name='validity',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
