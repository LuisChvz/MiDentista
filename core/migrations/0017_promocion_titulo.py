# Generated by Django 2.2.7 on 2019-12-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_promocion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='titulo',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
