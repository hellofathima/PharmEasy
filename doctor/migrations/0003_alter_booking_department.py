# Generated by Django 5.0.3 on 2024-04-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_booking_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Orthopedics', 'Orthopedics'), ('Neurology', 'Neurology'), ('Oncology', 'Oncology'), ('Pediatrics', 'Pediatrics'), ('Gynecology', 'Gynecology'), ('Dermatology', 'Dermatology')], default='Cardiology', max_length=100, null=True),
        ),
    ]