from django.urls import path
from fauna.apps.species import views

app_name = "species"

urlpatterns = [
    path(
        "admin/upload_species_data/",
        views.SpecieLoadDataView.as_view(),
        name="upload-species-data",
    ),
]
