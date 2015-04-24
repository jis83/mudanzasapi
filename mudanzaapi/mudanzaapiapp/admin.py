from django.contrib import admin

# Register your models here.


from mudanzaapiapp.models import *

class Campos_userAdmin(admin.ModelAdmin):
	list_display = ['user','telefonos','fotos','horario_de_contacto','dni','nombre_empresa']
	pass
admin.site.register(Campos_user, Campos_userAdmin)

class Solicitud_EnvioAdmin(admin.ModelAdmin):
	list_display = ['user','origen','destino','fecha_limite','desc_objetos','desc_lugar','escalera','ascensor','tipo_aviso']
	pass
admin.site.register(Solicitud_Envio, Solicitud_EnvioAdmin)

class PresupuestoAdmin(admin.ModelAdmin):
	list_display = ['solicitud_envio','user','valor','estado']
	pass
admin.site.register(Presupuesto, PresupuestoAdmin)