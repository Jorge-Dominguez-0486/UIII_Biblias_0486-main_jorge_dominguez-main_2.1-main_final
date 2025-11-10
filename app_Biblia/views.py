from django.shortcuts import render, redirect, get_object_or_404
# Importamos los TRES modelos
from .models import ClienteGlobal, Pedido, DetallePedido

def inicio_biblias(request):
    return render(request, 'inicio.html')

# ===================
# VISTAS PARA CLIENTE
# ===================
def agregar_cliente(request):
    if request.method == 'POST':
        ClienteGlobal.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            pais_residencia=request.POST.get('pais_residencia')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = ClienteGlobal.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.pais_residencia = request.POST.get('pais_residencia')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ===================
# VISTAS PARA PEDIDO
# ===================
def ver_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_hora')
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def agregar_pedido(request):
    clientes = ClienteGlobal.objects.all() 
    if request.method == 'POST':
        cliente_obj = get_object_or_404(ClienteGlobal, id=request.POST.get('cliente'))
        Pedido.objects.create(
            cliente=cliente_obj,
            total_neto=request.POST.get('total_neto', 0),
            metodo_pago=request.POST.get('metodo_pago'),
            estado_pedido=request.POST.get('estado_pedido', 'Pendiente'),
            impuesto_total=request.POST.get('impuesto_total', 0),
            costo_envio=request.POST.get('costo_envio', 0),
            direccion_envio=request.POST.get('direccion_envio')
        )
        return redirect('ver_pedidos')
    return render(request, 'pedido/agregar_pedido.html', {'clientes': clientes})

def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    clientes = ClienteGlobal.objects.all()
    context = {'pedido': pedido, 'clientes': clientes}
    return render(request, 'pedido/actualizar_pedido.html', context)

def realizar_actualizacion_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.cliente = get_object_or_404(ClienteGlobal, id=request.POST.get('cliente'))
        pedido.total_neto = request.POST.get('total_neto')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.estado_pedido = request.POST.get('estado_pedido')
        pedido.impuesto_total = request.POST.get('impuesto_total')
        pedido.costo_envio = request.POST.get('costo_envio')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.save()
        return redirect('ver_pedidos')
    clientes = ClienteGlobal.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido, 'clientes': clientes})

def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})

# ===================
# VISTAS PARA DETALLE_PEDIDO (NUEVO)
# ===================

def ver_detalles(request):
    detalles = DetallePedido.objects.all().order_by('pedido', 'numero_linea')
    return render(request, 'detalle_pedido/ver_detalles.html', {'detalles': detalles})

def agregar_detalle_pedido(request):
    pedidos = Pedido.objects.all() # Para el dropdown
    if request.method == 'POST':
        pedido_obj = get_object_or_404(Pedido, id=request.POST.get('pedido'))
        DetallePedido.objects.create(
            pedido=pedido_obj,
            producto_id=request.POST.get('producto_id'),
            numero_linea=request.POST.get('numero_linea'),
            cantidad=request.POST.get('cantidad', 1),
            precio_venta_unitario=request.POST.get('precio_venta_unitario', 0),
            subtotal_detalle=request.POST.get('subtotal_detalle', 0),
            porcentaje_descuento=request.POST.get('porcentaje_descuento', 0),
            impuesto_detalle=request.POST.get('impuesto_detalle', 0),
            notas_item=request.POST.get('notas_item')
        )
        return redirect('ver_detalles')
    return render(request, 'detalle_pedido/agregar_detalle_pedido.html', {'pedidos': pedidos})

def actualizar_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    pedidos = Pedido.objects.all()
    context = {'detalle': detalle, 'pedidos': pedidos}
    return render(request, 'detalle_pedido/actualizar_detalle_pedido.html', context)

def realizar_actualizacion_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    if request.method == 'POST':
        detalle.pedido = get_object_or_404(Pedido, id=request.POST.get('pedido'))
        detalle.producto_id = request.POST.get('producto_id')
        detalle.numero_linea = request.POST.get('numero_linea')
        detalle.cantidad = request.POST.get('cantidad')
        detalle.precio_venta_unitario = request.POST.get('precio_venta_unitario')
        detalle.subtotal_detalle = request.POST.get('subtotal_detalle')
        detalle.porcentaje_descuento = request.POST.get('porcentaje_descuento')
        detalle.impuesto_detalle = request.POST.get('impuesto_detalle')
        detalle.notas_item = request.POST.get('notas_item')
        detalle.save()
        return redirect('ver_detalles')
    
    pedidos = Pedido.objects.all()
    return render(request, 'detalle_pedido/actualizar_detalle_pedido.html', {'detalle': detalle, 'pedidos': pedidos})

def borrar_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalles')
    return render(request, 'detalle_pedido/borrar_detalle_pedido.html', {'detalle': detalle})