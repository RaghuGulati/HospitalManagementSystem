# Generated by Django 2.2.3 on 2020-05-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20200525_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='consultant_fees',
            field=models.IntegerField(default=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointments',
            name='other_fees',
            field=models.IntegerField(default=250),
            preserve_default=False,
        ),
    ]
