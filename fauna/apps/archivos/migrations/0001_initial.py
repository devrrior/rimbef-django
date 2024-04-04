# Generated by Django 3.1 on 2022-12-21 09:07

import fauna.apps.base.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=340, null=True, verbose_name='Nombre')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d', validators=[fauna.apps.base.validators.validate_file_size], verbose_name='Archivo')),
                ('note', models.CharField(blank=True, max_length=400, null=True, verbose_name='Nota')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'Propietario sensor',
                'verbose_name_plural': 'Propietarios archivos',
            },
        ),
    ]
