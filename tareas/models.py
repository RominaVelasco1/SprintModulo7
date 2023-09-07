from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

categorias = (
    ("1", "Trabajo"),
    ("2", "Hogar"),
    ("3", "Estudio"),
    ("4", "Otras categorías"),
)

estados = (
    ("1", "Pendiente"),
    ("2", "En progreso"),
    ("3", "Completada"),
)
PRIORIDADES = (
        ("1", 'Alta'),
        ("2", 'Baja'),
    )


class registroTareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    titulo_tarea = models.CharField(max_length=50, verbose_name="Título de tarea")
    descripcion_tarea = models.CharField(max_length=80, verbose_name="Descripción de tarea")    
    fecha_vencimiento_tarea = models.DateField(default=timezone.now, verbose_name="Fecha vencimiento tarea (dd-mm-yyyy)")
    categoria_tarea = models.CharField(max_length=1, choices=categorias, default='1', verbose_name="Categoria tarea") 
    estado_tarea = models.CharField(max_length=1, choices=estados, default='1', verbose_name="Estado de tarea")
    observaciones_tarea = models.TextField(max_length=300)
    prioridad= models.CharField(max_length=1, choices=PRIORIDADES, default='1', verbose_name="Prioridad tarea")
    # Agrega un campo para asignar la tarea a un usuario
    asignada_a = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Asignada a")

            
    def __str__(self):
        return "Id: %s, Nombre Tarea: %s, Descripción tarea: %s,  Vencimiento tarea: %s, Categoria: %s, Estado: %s,  Asignada a: %s, Observaciones: %s, Prioridad: %s" %(
            self.id_tarea, 
            self.titulo_tarea, 
            self.descripcion_tarea, 
            self.fecha_vencimiento_tarea, 
            self.categoria_tarea, 
            self.estado_tarea,
            self.asignada_a.username if self.asignada_a else "Sin asignar",  # Mostrar el nombre de usuario o "Sin asignar" si no se asigna a un usuario
            self.observaciones_tarea,
            self.prioridad)
    
class Prioridad(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Prioridad")

    def __str__(self):
        return self.nombre

