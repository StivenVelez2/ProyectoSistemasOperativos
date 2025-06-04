from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('crear/', views.reporte_create, name='reporte_create'),
    path('lista/', views.reporte_list, name='reporte_list'),
    path('detalle/<int:pk>/', views.reporte_detail, name='reporte_detail'), 
    path('editar/<int:pk>/', views.reporte_update, name='reporte_update'),
    path('eliminar/<int:pk>/', views.reporte_delete, name='reporte_delete'),
]
