from django.contrib import admin
# Importamos los 3 modelos
from .models import ClienteGlobal, Pedido, DetallePedido

admin.site.register(ClienteGlobal)
admin.site.register(Pedido)
# Agregamos esta línea
admin.site.register(DetallePedido)