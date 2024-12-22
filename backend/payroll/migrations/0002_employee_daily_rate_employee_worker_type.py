# Generated by Django 5.1.4 on 2024-12-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='daily_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='worker_type',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('daily', 'Daily')], default='hourly', max_length=10),
        ),
    ]
