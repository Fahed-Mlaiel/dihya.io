from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transport/', include('Dihya.backend.django.app.routes.transport.urls')),
    path('api/logistique/', include('Dihya.backend.django.app.routes.logistique.urls')),
    # Weitere Business-Module hier einbinden...
]
