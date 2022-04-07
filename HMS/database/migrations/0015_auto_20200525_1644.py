# Generated by Django 2.2.3 on 2020-05-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_prescriptions_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='medicines',
            field=models.CharField(default='no medicine', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='prescription_medicines',
        ),
    ]