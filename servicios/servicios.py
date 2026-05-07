from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(

        self,
        nombre,
        precio

    ):

        self.nombre = nombre
        self.precio = precio

        self.disponible = True

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# ======================================
# RESERVA SALA
# ======================================

class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__(
            "Reserva Sala",
            50000
        )

        self.horas = horas

    def calcular_costo(self):

        return (
            self.precio *
            self.horas
        )

    def descripcion(self):

        return (
            f"Sala reservada "
            f"{self.horas} horas"
        )


# ======================================
# ALQUILER EQUIPO
# ======================================

class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__(
            "Alquiler Equipo",
            30000
        )

        self.dias = dias

    def calcular_costo(self):

        return (
            self.precio *
            self.dias
        )

    def descripcion(self):

        return (
            f"Equipo alquilado "
            f"{self.dias} días"
        )


# ======================================
# ASESORÍA
# ======================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, sesiones):

        super().__init__(
            "Asesoría Especializada",
            80000
        )

        self.sesiones = sesiones

    def calcular_costo(self):

        return (
            self.precio *
            self.sesiones
        )

    def descripcion(self):

        return (
            f"Asesoría "
            f"{self.sesiones} sesiones"
        )