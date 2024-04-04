import logging

from django.contrib import admin, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from fauna.apps.base.destination import DestinationFile
from fauna.apps.base.models import BaseModel
from fauna.apps.species import forms, models, record

logger = logging.getLogger(__name__)


@method_decorator([staff_member_required], name="dispatch")
class SpecieLoadDataView(FormView):
    form_class = forms.SensorLoadDataForm
    template_name = "admin/upload_species_data.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        admin_context = admin.site.each_context(self.request)
        context.update(admin_context)
        context.update(
            {
                "title": "Subir Data",
            }
        )
        return context

    def form_valid(self, form):  # noqa
        try:
            collection_file = form.cleaned_data["collection_file"]
            destination = DestinationFile(collection_file)
            destination.destination()
            records_list = record._generate_species_data_from_file_record(file=collection_file)
            rows = record.add_massive_data(records_list)
            success = rows["success"]
            errors = rows["errors"]
            messages.add_message(
                self.request, messages.SUCCESS, f"{success} registros agregados."
            )
            messages.add_message(
                self.request, messages.ERROR, f"{errors} registros no agregados."
            )
            return self.render_to_response(self.get_context_data(request=self.request, form=form))
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, f"{e}")
            return self.form_invalid(form)

