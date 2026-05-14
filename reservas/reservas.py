from excepciones import (
    ErrorReserva,
    registrar_info,
    registrar_error
)


class Reserva:

    lista_reservas = []

    def __init__(

        self,
        id_reserva,
        cliente,
        servicio,
        cantidad,
        descuento=0.0

    ):

        self.id_reserva = id_reserva

        self.cliente = cliente

        self.servicio = servicio

        self.cantidad = cantidad

        self.descuento = descuento

        self.estado = "Pendiente"

        self.pagado = False

        self.costo_total = self.calcular_total()

        Reserva.lista_reservas.append(self)

    # ==================================
    # CONFIRMAR
    # ==================================

    def confirmar(self):

        try:

            if not self.servicio.disponible:

                raise ErrorReserva(
                    "Servicio no disponible"
                )

            self.estado = "Confirmada"

            registrar_info(

                f"Reserva confirmada "
                f"para {self.cliente.nombre}"

            )

        except ErrorReserva as error:

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

            raise ErrorReserva(
                "La reserva no está confirmada"
            )

        self.pagado = True

        self.estado = "Procesada"

        registrar_info(

            f"Pago realizado "
            f"por {self.cliente.nombre}"

        )

    # ==================================
    # CALCULAR TOTAL
    # ==================================

    def calcular_total(self):

        return self.servicio.calcular_costo(

            self.cantidad,
            descuento=self.descuento

        )

    # ==================================
    # MOSTRAR
    # ==================================

    def mostrar_reserva(self):

        return (

            f"\nCliente: {self.cliente.nombre}\n"

            f"Servicio: {self.servicio.nombre}\n"

            f"Estado: {self.estado}\n"

            f"Pagado: {self.pagado}\n"

            f"Total: ${self.costo_total:,.2f}"

        )