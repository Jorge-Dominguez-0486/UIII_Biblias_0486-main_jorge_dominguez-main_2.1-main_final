from django.db import models

# MODELO: CLIENTE_GLOBAL
class ClienteGlobal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_residencia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

# ===================
# MODELO: PEDIDO
# ===================
class Pedido(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=50)
    estado_pedido = models.CharField(max_length=50, default='Pendiente')
    impuesto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion_envio = models.CharField(max_length=255)
    cliente = models.ForeignKey(
        ClienteGlobal,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )

    def __str__(self):
        return f"Pedido #{self.pk} - Cliente: {self.cliente.apellido}"

# ===================
# MODELO: DETALLE_PEDIDO (Tercera Parte)
# ===================
class DetallePedido(models.Model):
    cantidad = models.PositiveIntegerField(default=1)
    precio_venta_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_detalle = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impuesto_detalle = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notas_item = models.CharField(max_length=255, blank=True, null=True)
    numero_linea = models.PositiveIntegerField()
    producto_id = models.IntegerField() # Como indica el PDF, lo dejamos como Integer

    # Relación 1 a N: Un pedido tiene muchos detalles
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    class Meta:
        verbose_name_plural = "Detalles de Pedido"
        ordering = ['pedido', 'numero_linea']

    def __str__(self):
        return f"Detalle de Pedido #{self.pedido.pk}, Línea {self.numero_linea}"