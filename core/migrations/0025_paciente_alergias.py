# Generated by Django 2.2.7 on 2019-12-02 19:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20191201_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='alergias',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, null=True),
        ),
    ]
