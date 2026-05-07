from excepciones import (
ReservaError,
registrar_info,
registrar_error
)


class Reserva:

lista_reservas = []

def __init__(

self,
cliente,
servicio

):

self.cliente = cliente

self.servicio = servicio

self.estado = "Pendiente"

self.pagado = False

Reserva.lista_reservas.append(self)

# ==================================
# CONFIRMAR
# ==================================

def confirmar(self):

try:

if not self.servicio.disponible:

raise ReservaError(
"Servicio no disponible"
)

self.estado = "Confirmada"

registrar_info(

f"Reserva confirmada "
f"para {self.cliente.nombre}"

)

except ReservaError as error:

registrar_error(str(error))

raise

# ==================================
# CANCELAR
# ==================================

def cancelar(self):

self.estado = "Cancelada"

registrar_info(

f"Reserva cancelada "
f"para {self.cliente.nombre}"

)

# ==================================
# PAGAR
# ==================================

def pagar(self):

if self.estado != "Confirmada":

raise ReservaError(
"La reserva no está confirmada"
)

self.pagado = True

registrar_info(

f"Pago realizado "
f"por {self.cliente.nombre}"

)

# ==================================
# CALCULAR TOTAL
# ==================================

def calcular_total(

self,
impuesto=0,
descuento=0

):

total = self.servicio.calcular_costo()

total += total * impuesto

total -= descuento

return total

# ==================================
# MOSTRAR RESERVA
# ==================================

def mostrar_reserva(self):

return (

f"\nCliente: {self.cliente.nombre}\n"

f"Servicio: {self.servicio.nombre}\n"

f"Estado: {self.estado}\n"

f"Pagado: {self.pagado}"

)
