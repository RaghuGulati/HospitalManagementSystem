# Generated by Django 2.2.3 on 2020-05-24 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200524_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='age',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='patients_medical_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('blood_group', models.CharField(max_length=5)),
                ('allergies', models.CharField(max_length=250)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.patients')),
            ],
        ),
    ]