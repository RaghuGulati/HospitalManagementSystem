# Generated by Django 2.2.3 on 2020-05-25 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_payment_history_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='doctor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.doctor'),
            preserve_default=False,
        ),
    ]
