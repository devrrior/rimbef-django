from django.conf import settings

from django.contrib.admin import ModelAdmin, register
from fauna.apps.observations import models


@register(models.Sex)
class SexAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "leak_add"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.StageLife)
class StageLifeAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "update"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Source)
class SourceClassAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "folder"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Method)
class MethodAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "layers"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.ActivitySpeciesObservation)
class ActivitySpeciesObservationAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    icon_name = "view_day"
    list_per_page = settings.NUMBER_PAGINATION_ADMIN


@register(models.Observation)
class ObservationClassAdmin(ModelAdmin):
    list_display = ("id", "specie", "observation_date")
    search_fields = ("place", "method", "observation_type",)
    ordering = ("id",)
    icon_name = "remove_red_eye"
    date_hierarchy = "observation_date"
    raw_id_fields = (
        "specie",
        "sources",
        "method",
        "activity",
        "habitat",
        "state",
        "sex", "stage_life",
    )
    list_per_page = settings.NUMBER_PAGINATION_ADMIN
