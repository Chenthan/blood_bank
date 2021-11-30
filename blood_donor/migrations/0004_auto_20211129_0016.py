# Generated by Django 3.2.8 on 2021-11-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donor', '0003_remove_blooddonor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='blooddonor',
            name='blood_group',
            field=models.CharField(choices=[(1, 'A+'), (2, 'A−'), (3, 'B+'), (4, 'B−'), (5, 'AB+'), (6, 'AB−'), (7, 'O+'), (8, 'O−')], default=1, max_length=10),
        ),
    ]