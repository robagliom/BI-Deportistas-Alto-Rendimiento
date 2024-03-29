# Generated by Django 3.1.4 on 2020-12-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permiso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=8, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('permisos', models.ManyToManyField(to='permiso.Permiso')),
            ],
        ),
    ]
