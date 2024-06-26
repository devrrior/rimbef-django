# Generated by Django 3.1 on 2023-10-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0004_auto_20231018_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specie',
            name='cites',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Cites'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='distribution',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Distribución'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='invasion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Invasión'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='residence',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Residencia'),
        ),
    ]
