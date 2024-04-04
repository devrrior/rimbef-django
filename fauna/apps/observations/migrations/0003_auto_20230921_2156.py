# Generated by Django 3.1 on 2023-09-21 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0003_auto_20230921_2155'),
        ('observations', '0002_auto_20230620_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySpeciesObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Metodo',
                'verbose_name_plural': 'Metodos',
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Metodo',
                'verbose_name_plural': 'Metodos',
            },
        ),
        migrations.AlterModelOptions(
            name='observation',
            options={'verbose_name': 'Observación', 'verbose_name_plural': 'Observaciones'},
        ),
        migrations.RemoveField(
            model_name='observation',
            name='life_stage',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='microhabitat',
        ),
        migrations.AlterField(
            model_name='observation',
            name='distance',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Distancia'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='habitat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='habitat_observation', to='species.habitat', verbose_name='Habitat'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='indqty',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='latitude',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='longitude',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='observation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='observation_type',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='place',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Lugar'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specie_status_observation', to='species.speciestatus', verbose_name='Estado especie'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='activity_observation', to='observations.activityspeciesobservation', verbose_name='Actividad observaciòn'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='method_observation', to='observations.method', verbose_name='Mètodo'),
        ),
    ]