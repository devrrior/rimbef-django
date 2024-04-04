from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # Temporary redirect
    path("", RedirectView.as_view(url="admin/")),
    path("", include("fauna.apps.archivos.urls")),
    path("", include("fauna.apps.species.urls")),
]
