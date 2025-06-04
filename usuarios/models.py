from django.db import models
from django.contrib.auth.models import User

class Reporte(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportes_usuarios')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
