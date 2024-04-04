from django.conf import settings

from django.contrib.admin import ModelAdmin, register
from fauna.apps.species import models


@register(models.SocialStructure)
class SocialStructureAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "insert_invitation"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.TrophyGuild)
class TrophyGuildAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "filter_frames"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.SpecieStatus)
class SpecieStatusAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "check_circle"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Habitat)
class HabitatAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "landscape"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Kingdom)
class KingdomAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "star_half"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Phylum)
class PhylumAdmin(ModelAdmin):
    list_display = ("id", "name", "kingdom")
    search_fields = ("name", "kingdom",)
    ordering = ("id",)
    icon_name = "list"
    raw_id_fields = (
        "kingdom",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.SpecieClass)
class SpecieClassAdmin(ModelAdmin):
    list_display = ("id", "name", "ecology_group", "phylum")
    search_fields = ("name", "ecology_group",)
    ordering = ("id",)
    icon_name = "apps"
    raw_id_fields = (
        "phylum",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Order)
class OrderAdmin(ModelAdmin):
    list_display = ("id", "name", "specie_class")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "reorder"
    raw_id_fields = (
        "specie_class",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Family)
class FamilyAdmin(ModelAdmin):
    list_display = ("id", "name", "order")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "group_work"
    raw_id_fields = (
        "order",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Genus)
class GenusAdmin(ModelAdmin):
    list_display = ("id", "name", "family")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "compare_arrows"
    raw_id_fields = (
        "family",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Specie)
class SpecieAdmin(ModelAdmin):
    list_display = ("id", "common_name", "scientific_name", "genus", "taxon_id_rimfeb")
    search_fields = ("common_name", "scientific_name",)
    ordering = ("id",)
    icon_name = "pets"
    raw_id_fields = (
        "genus", "social_structure", "trophic_guild",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN
