# Generated by Django 2.2.3 on 2020-05-25 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_prescriptions_doctor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients_medical_report',
            name='case_paper',
        ),
    ]
