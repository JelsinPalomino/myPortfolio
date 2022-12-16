from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('form/', views.CreateProyectos.as_view(), name='form'),
    path('delete/<int:id>', views.deleteProyecto, name='delete'),
    # path('proyectDetalles/<int:id>', views.proyectDetalles, name='detalles')
]