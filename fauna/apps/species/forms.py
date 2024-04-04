from django import forms


class SensorLoadDataForm(forms.Form):
    collection_file = forms.FileField(required=True, label="Elija el archivo")
