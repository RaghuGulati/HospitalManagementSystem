# Generated by Django 2.2.3 on 2020-05-25 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_patient_notifications_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='app_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.appointments'),
            preserve_default=False,
        ),
    ]