# Generated by Django 3.1.4 on 2021-02-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datoobjetivo', '0003_datoobjetivo_velmayor25'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoobjetivo',
            name='totalTime',
            field=models.CharField(max_length=15, null=True),
        ),
    ]