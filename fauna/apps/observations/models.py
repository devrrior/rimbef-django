from django.db import models

from fauna.apps.base.models import BaseModel
from fauna.apps.species.models import Specie, Habitat, SpecieStatus


class Sex(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"


class StageLife(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Etapa de vida"
        verbose_name_plural = "Etapas de vida"


class Source(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)
    description = models.CharField(max_length=150, verbose_name="Descripción", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Fuente"
        verbose_name_plural = "Fuentes"


class Method(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Mètodo"
        verbose_name_plural = "Mètodos"


class ActivitySpeciesObservation(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"


class Observation(BaseModel):
    specie = models.ForeignKey(
        Specie,
        on_delete=models.PROTECT,
        verbose_name="Especie",
        related_name="specie_observation"
    )
    observation_date = models.DateField(verbose_name="Fecha", null=True, blank=True)
    place = models.CharField(max_length=150, verbose_name="Lugar", null=True, blank=True)
    distance = models.CharField(max_length=150, verbose_name="Distancia", null=True, blank=True)
    latitude = models.CharField(max_length=150, verbose_name="Latitud", null=True, blank=True)
    longitude = models.CharField(max_length=150, verbose_name="Longitud", null=True, blank=True)
    observation_type = models.CharField(max_length=150, verbose_name="Tipo", null=True, blank=True)
    indqty = models.CharField(max_length=150, null=True, blank=True)
    url_photo = models.CharField(max_length=150, verbose_name="Url foto", null=True, blank=True)
    url_web = models.CharField(max_length=150, verbose_name="Url web", null=True, blank=True)
    license = models.CharField(max_length=150, verbose_name="Licencia", null=True, blank=True)
    method = models.ForeignKey(
        Method,
        on_delete=models.PROTECT,
        verbose_name="Mètodo",
        related_name="method_observation",
        null=True,
        blank=True
    )
    activity = models.ForeignKey(
        ActivitySpeciesObservation,
        on_delete=models.PROTECT,
        verbose_name="Actividad observaciòn",
        related_name="activity_observation",
        null=True,
        blank=True
    )
    habitat = models.ForeignKey(
        Habitat,
        on_delete=models.PROTECT,
        verbose_name="Habitat",
        related_name="habitat_observation",
        null=True,
        blank=True
    )
    state = models.ForeignKey(
        SpecieStatus,
        on_delete=models.PROTECT,
        verbose_name="Estado especie",
        related_name="specie_status_observation",
        null=True,
        blank=True
    )
    sex = models.ForeignKey(
        Sex,
        on_delete=models.PROTECT,
        verbose_name="Sexo",
        related_name="sex_specie",
        null=True,
        blank=True
    )
    stage_life = models.ForeignKey(
        StageLife,
        on_delete=models.PROTECT,
        verbose_name="Ètapa de la vida",
        related_name="stage_life_specie",
        null=True,
        blank=True
    )
    sources = models.ManyToManyField(
        Source, related_name="sources_observations", verbose_name="Fuentes"
    )

    def __str__(self):
        return f"{self.specie} - {self.observation_date}"

    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"
