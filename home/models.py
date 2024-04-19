# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vehiculo(models.Model):

    #__Vehiculo_FIELDS__
    marca = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    placa = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)

    #__Vehiculo_FIELDS__END

    class Meta:
        verbose_name        = _("Vehiculo")
        verbose_name_plural = _("Vehiculo")


class Propietario(models.Model):

    #__Propietario_FIELDS__
    nombres = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Propietario_FIELDS__END

    class Meta:
        verbose_name        = _("Propietario")
        verbose_name_plural = _("Propietario")


class Revision(models.Model):

    #__Revision_FIELDS__
    obsertvaciones = models.CharField(max_length=255, null=True, blank=True)

    #__Revision_FIELDS__END

    class Meta:
        verbose_name        = _("Revision")
        verbose_name_plural = _("Revision")


class Ordenreparacion(models.Model):

    #__Ordenreparacion_FIELDS__

    #__Ordenreparacion_FIELDS__END

    class Meta:
        verbose_name        = _("Ordenreparacion")
        verbose_name_plural = _("Ordenreparacion")


class Solicitud_Reparacion(models.Model):

    #__Solicitud_Reparacion_FIELDS__
    detalle = models.CharField(max_length=255, null=True, blank=True)

    #__Solicitud_Reparacion_FIELDS__END

    class Meta:
        verbose_name        = _("Solicitud_Reparacion")
        verbose_name_plural = _("Solicitud_Reparacion")


class Item_Vehiculo(models.Model):

    #__Item_Vehiculo_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    fecha_fin = models.CharField(max_length=255, null=True, blank=True)

    #__Item_Vehiculo_FIELDS__END

    class Meta:
        verbose_name        = _("Item_Vehiculo")
        verbose_name_plural = _("Item_Vehiculo")


class Servicio(models.Model):

    #__Servicio_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Servicio_FIELDS__END

    class Meta:
        verbose_name        = _("Servicio")
        verbose_name_plural = _("Servicio")


class Diagnostico(models.Model):

    #__Diagnostico_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Diagnostico_FIELDS__END

    class Meta:
        verbose_name        = _("Diagnostico")
        verbose_name_plural = _("Diagnostico")


class Respuesto(models.Model):

    #__Respuesto_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Respuesto_FIELDS__END

    class Meta:
        verbose_name        = _("Respuesto")
        verbose_name_plural = _("Respuesto")


class Undefined(models.Model):

    #__Undefined_FIELDS__

    #__Undefined_FIELDS__END

    class Meta:
        verbose_name        = _("Undefined")
        verbose_name_plural = _("Undefined")



#__MODELS__END
