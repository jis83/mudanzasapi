from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from mudanzaapiapp.models import *

from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class Campos_userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campos_user
        fields = ('user','telefonos','fotos','horario_de_contacto','dni','nombre_empresa')
class Solicitud_EnvioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitud_Envio
        fields = ('user','origen','destino','fecha_limite','desc_objetos','desc_lugar','escalera','ascensor','tipo_aviso')
class PresupuestoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Presupuesto
        fields = ('solicitud_envio','user','valor','estado')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class Campos_userViewSet(viewsets.ModelViewSet):
    queryset = Campos_user.objects.all()
    serializer_class = Campos_userSerializer
class Solicitud_EnvioViewSet(viewsets.ModelViewSet):
	queryset = Solicitud_Envio.objects.all()
	serializer_class = Solicitud_EnvioSerializer
class PresupuestoViewSet(viewsets.ModelViewSet):
	queryset = Presupuesto.objects.all()
	serializer_class = PresupuestoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'campos_user', Campos_userViewSet)
router.register(r'solicitudes', Solicitud_EnvioViewSet)
router.register(r'presupuestos', PresupuestoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mudanzaapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
