# Generated by Django 2.2.7 on 2019-11-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191130_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(blank=True, upload_to='publicaciones/%Y/%m/%D/'),
        ),
    ]