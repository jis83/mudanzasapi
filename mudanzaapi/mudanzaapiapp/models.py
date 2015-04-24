from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Campos_user(models.Model):
    """
    Clase Campos_user para agregar campos a la clase User
    """
    # Relacion uno a uno con tabla User de Django para poder extenderla
    user = models.OneToOneField(User)
    telefonos = models.CharField(max_length=200)  # Usuario y Cliente
    fotos = models.CharField(max_length=200)  # Usuario y Cliente
    horario_de_contacto = models.CharField(max_length=200)  # Usuario
    dni = models.CharField(max_length=200)  # Usuario
    nombre_empresa = models.CharField(max_length=200)  # Cliente

    def get_absolute_url(self):
        return reverse('detail_camposuser', kwargs={'pk': self.id})


class Solicitud_Envio(models.Model):
    user = models.ForeignKey(User)  # Usuario que genero la solicitud
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    # Fecha limite para el traslado
    fecha_limite = models.DateTimeField('date published')
    # Descripcion de los objetos a transportar
    desc_objetos = models.CharField(max_length=200)
    # Descripcion del lugar a donde se llevaran
    desc_lugar = models.CharField(max_length=200)
    escalera = models.CharField(max_length=200)  # SI/NO
    ascensor = models.CharField(max_length=200)  # SI/NO
    # Subasta o presupuesto normal
    tipo_aviso = models.CharField(max_length=200)


class Presupuesto(models.Model):
    # Solicitud de Envio a la que corresponde el presupuesto
    solicitud_envio = models.ForeignKey(Solicitud_Envio)
    # Cliente que realizo el presupuesto
    user = models.ForeignKey(User)
    valor = models.FloatField(max_length=200)
    # (Estado inicial)/ACEPTADO (Usuario acepto preupuesto)/PAGADO
    # (Cliente pago)
    estado = models.CharField(max_length=200)