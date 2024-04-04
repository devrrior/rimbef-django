from django.db import models

from fauna.apps.base.models import BaseModel


class SocialStructure(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Estructura social"
        verbose_name_plural = "Estructuras sociales"


class TrophyGuild(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Gremio trofico"
        verbose_name_plural = "Gremios troficos"


class SpecieStatus(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Estado especie"
        verbose_name_plural = "Estados de las especies"


class Habitat(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Habitat"
        verbose_name_plural = "Habitats"


class Kingdom(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Reino"
        verbose_name_plural = "Reinos"


class Phylum(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)
    code = models.CharField(max_length=150, verbose_name="Còdigo", null=True, blank=True)
    kingdom = models.ForeignKey(
        Kingdom,
        on_delete=models.PROTECT,
        verbose_name="Reino",
        related_name="kingdom_specie"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Phylum"
        verbose_name_plural = "Phylums"


class SpecieClass(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    ecology_group = models.CharField(max_length=150, verbose_name="Grupo ecologico")
    phylum = models.ForeignKey(
        Phylum,
        on_delete=models.PROTECT,
        verbose_name="Phylum",
        related_name="phylum_specie_class",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"


class Order(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    specie_class = models.ForeignKey(
        SpecieClass,
        on_delete=models.PROTECT,
        verbose_name="Clase",
        related_name="specie_class_specie_order"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"


class Family(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        verbose_name="Orden",
        related_name="specie_order_specie_family"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"


class Genus(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    family = models.ForeignKey(
        Family,
        on_delete=models.PROTECT,
        verbose_name="Familia",
        related_name="specie_family_specie_genus"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"


class Specie(BaseModel):
    scientific_name = models.CharField(max_length=250, verbose_name="Nombre científico")
    common_name = models.CharField(max_length=150, verbose_name="Nombre común")
    uicn = models.CharField(max_length=150, verbose_name="UICN")
    cites = models.CharField(max_length=150, verbose_name="Cites", null=True, blank=True)
    distribution = models.CharField(max_length=100, verbose_name="Distribución", null=True, blank=True)
    invasion = models.CharField(max_length=100, verbose_name="Invasión", null=True, blank=True)
    residence = models.CharField(max_length=100, verbose_name="Residencia", null=True, blank=True)
    taxon_id_rimfeb = models.IntegerField(null=True, blank=True)
    genus = models.ForeignKey(
        Genus,
        on_delete=models.PROTECT,
        verbose_name="Género",
        related_name="genus_specie"
    )
    social_structure = models.ForeignKey(
        SocialStructure,
        on_delete=models.PROTECT,
        verbose_name="Estructura social",
        related_name="social_structure_specie",
        null=True,
        blank=True
    )
    trophic_guild = models.ForeignKey(
        TrophyGuild,
        on_delete=models.PROTECT,
        verbose_name="Gremio Tròfico",
        related_name="trophic_guild_specie",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.common_name}"

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"
