from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from demanda.urls import routerDemanda
from administrativo.urls import routerAdministrativo
from regra_email.urls import routerEmail

urlpatterns = [
                  path('', include('core.urls')),
                  path('api/demanda/', include(routerDemanda.urls)),
                  path('api/administrativo/', include(routerAdministrativo.urls)),
                  path('painel/', admin.site.urls),
                  path('api/regraemail/', include(routerEmail.urls)),
                  path('api-auth/', include('rest_framework.urls')),
                  path('auths/', include('django.contrib.auth.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
