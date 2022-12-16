from django.shortcuts import render, redirect
from .models import Proyectos
from .forms import ProyectoForm
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import json

# Creamos el Index
class Index(TemplateView):
    extra_context = {'form': Proyectos.objects.all()}
    template_name = 'index.html'

    def get_context_data(self):
        context = {}
        context['proyectos'] = Proyectos.objects.all()
        return context

# Creamos CreateProyectos(FormView)
class CreateProyectos(LoginRequiredMixin, FormView):
    model = Proyectos
    template_name = "form.html"
    form_class = ProyectoForm
    
    # Guardar la info a la BD
    def form_valid(self, form):
        Proyectos.objects.create(**form.cleaned_data)
        return redirect('index')


def proyectDetalles(request, id):
    projects = Proyectos.objects.get(id=id)
    context = {
        "projects", projects
    }
    print(type(projects))
    print(context)
    return render(request, 'proyectDetalles.html', context)

@login_required
def deleteProyecto(request, id):
    proyecto = Proyectos.objects.get(id=id)
    proyecto.delete()
    return redirect('index')

