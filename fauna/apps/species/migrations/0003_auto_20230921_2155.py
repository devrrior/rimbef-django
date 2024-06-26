# Generated by Django 3.1 on 2023-09-21 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_auto_20230620_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Habitat',
                'verbose_name_plural': 'Habitats',
            },
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Reino',
                'verbose_name_plural': 'Reinos',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
            },
        ),
        migrations.CreateModel(
            name='SocialStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estructura social',
                'verbose_name_plural': 'Estructuras sociales',
            },
        ),
        migrations.CreateModel(
            name='SpecieStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estado especie',
                'verbose_name_plural': 'Estados de las especies',
            },
        ),
        migrations.CreateModel(
            name='StageLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Etapa de vida',
                'verbose_name_plural': 'Etapas de vida',
            },
        ),
        migrations.CreateModel(
            name='TrophyGuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Gremio trofico',
                'verbose_name_plural': 'Gremios troficos',
            },
        ),
        migrations.RemoveField(
            model_name='specie',
            name='trophic_grame',
        ),
        migrations.AddField(
            model_name='specie',
            name='taxon_id_rimfeb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='genus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genus_specie', to='species.genus', verbose_name='Género'),
        ),
        migrations.CreateModel(
            name='Phylum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='kingdom_specie', to='species.kingdom', verbose_name='Reino')),
            ],
            options={
                'verbose_name': 'Phylum',
                'verbose_name_plural': 'Phylums',
            },
        ),
        migrations.AddField(
            model_name='specie',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sex_specie', to='species.sex', verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='specie',
            name='stage_life',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stage_life_specie', to='species.stagelife', verbose_name='Ètapa de la vida'),
        ),
        migrations.AddField(
            model_name='specie',
            name='trophic_guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trophic_guild_specie', to='species.trophyguild', verbose_name='Gremio Tròfico'),
        ),
        migrations.AddField(
            model_name='specieclass',
            name='phylum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phylum_specie_class', to='species.phylum', verbose_name='Phylum'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='social_structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='social_structure_specie', to='species.socialstructure', verbose_name='Estructura social'),
        ),
    ]
