# Generated by Django 2.2.7 on 2019-11-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191127_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
