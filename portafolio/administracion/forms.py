from django import forms

class ProyectoForm(forms.Form):
    title       = forms.CharField(max_length = 100, required=True)
    foto        = forms.CharField(max_length = 1000, help_text="Ingrese el URL de la imagen", required=True)
    description = forms.CharField(max_length = 100, help_text="Ingrese la descripción del proyecto", required=True)
    tags        = forms.CharField(max_length = 100, help_text="HTML, CSS, PYTHON, etc.", required=True)
    url         = forms.CharField(max_length = 1000, help_text="Ingrese el URL del proyecto" , required=True)
