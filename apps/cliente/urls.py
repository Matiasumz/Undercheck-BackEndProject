from django.urls import path
from .views import ClienteView   , ClienteFormView, HomeClienteView

urlpatterns = [
    path("inicio", HomeClienteView.as_view(), name="cliente_inicio"),
    path("<int:id>", ClienteView.as_view(), name="cliente"),
    path("crear", ClienteFormView.as_view(), name="crear_cliente"),
    # otras URLs de la aplicación
]
