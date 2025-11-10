from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_biblias, name='inicio_biblias'),
    
    # Rutas de Cliente
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Rutas de Pedido
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/actualizar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('pedidos/borrar/<int:id>/', views.borrar_pedido, name='borrar_pedido'),

    # --- AGREGAR ESTAS RUTAS PARA DETALLES ---
    path('detalles/', views.ver_detalles, name='ver_detalles'),
    path('detalles/agregar/', views.agregar_detalle_pedido, name='agregar_detalle_pedido'),
    path('detalles/actualizar/<int:id>/', views.actualizar_detalle_pedido, name='actualizar_detalle_pedido'),
    path('detalles/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_detalle_pedido, name='realizar_actualizacion_detalle_pedido'),
    path('detalles/borrar/<int:id>/', views.borrar_detalle_pedido, name='borrar_detalle_pedido'),
]