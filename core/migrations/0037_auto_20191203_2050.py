# Generated by Django 2.2.7 on 2019-12-04 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20191203_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='asignada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cita',
            name='atendida',
            field=models.BooleanField(default=False),
        ),
    ]
