from django.db import models
from django.conf import settings

class Reporte(models.Model):
    usuario_id = models.IntegerField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'dashboard'