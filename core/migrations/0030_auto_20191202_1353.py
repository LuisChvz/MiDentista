# Generated by Django 2.2.7 on 2019-12-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_delete_alergia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='medicamento',
        ),
        migrations.AddField(
            model_name='receta',
            name='medicamento',
            field=models.ManyToManyField(to='core.Medicamento'),
        ),
    ]
