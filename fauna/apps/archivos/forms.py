from datetime import datetime

from django import forms
from fauna.apps.archivos import constants


class SensorLoadDataForm(forms.Form):
    Options = (
        (constants.ALPHANSENSE, "Alphasense"),
        (constants.CLARITY, "Clarity"),
        (constants.DAVIS, "Davis"),
        (constants.TSILINK, "Linktsi"),
        (constants.URADMONITOR, "Uradmonitor"),
        (constants.UCENTRAL, "Ucentral"),
        (constants.PURPLEAIR, "Purple Air"),
    )
    collection_file = forms.FileField(
        required=True, label="Elija el archivo del sensor"
    )
    code = forms.CharField(
        label="Código del Sensor",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Código del Sensor"}),
    )
    category = forms.ChoiceField(label="Marca", widget=forms.Select, choices=Options)
    start_date = forms.DateField(
        initial=datetime.now().date(),
        widget=forms.DateTimeInput(format=("%d/%m/%Y")),
        required=False,
    )
    end_date = forms.DateTimeField(
        initial=datetime.now(),
        widget=forms.DateTimeInput(format=("%d/%m/%Y %H:%M:%S")),
        required=False,
    )
