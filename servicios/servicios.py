"""
=============================================================
  servicios.py — Clases de servicios Software FJ
=============================================================
"""

from abc import ABC, abstractmethod
from excepciones import ErrorServicio, ErrorParametro, ErrorDisponibilidad


# ======================================
# CLASE ABSTRACTA BASE
# ======================================
class Servicio(ABC):

    IVA = 0.19  # 19% IVA Colombia

    def __init__(self, id_servicio: str, nombre: str, precio_hora: float):

        if not id_servicio or not isinstance(id_servicio, str):
            raise ErrorParametro("El ID del servicio no puede estar vacío.")

        if not nombre or len(nombre.strip()) < 3:
            raise ErrorServicio("El nombre del servicio debe tener al menos 3 caracteres.")

        if not isinstance(precio_hora, (int, float)) or precio_hora <= 0:
            raise ErrorServicio("El precio por hora debe ser un número positivo.")

        self._id_servicio = id_servicio
        self._nombre      = nombre.strip()
        self._precio_hora = float(precio_hora)
        self._disponible  = True

    # ── propiedades ───────────────────────────────────────────
    @property
    def id_servicio(self):
        return self._id_servicio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_hora(self):
        return self._precio_hora

    @property
    def disponible(self):
        return self._disponible

    # ── calcular_costo (parámetros opcionales = sobrecarga) ───
    def calcular_costo(self, horas: float,
                       descuento: float = 0.0,
                       aplicar_iva: bool = True) -> float:
        try:
            if horas <= 0:
                raise ErrorParametro("Las horas deben ser un valor positivo.")
            base  = self._precio_hora * horas
            base  = max(0.0, base - descuento)
            total = base * (1 + self.IVA) if aplicar_iva else base
            return round(total, 2)
        except ErrorParametro:
            raise
        except Exception as e:
            raise ErrorServicio(f"Error en cálculo de costo: {e}") from e

    @abstractmethod
    def validar_parametros(self, horas: float) -> bool:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass

    def __str__(self):
        return self.descripcion()


# ======================================
# RESERVA SALA
# ======================================
class ReservaSala(Servicio):

    MAX_HORAS = 12

    def __init__(self, id_servicio: str, nombre: str,
                 precio_hora: float, capacidad: int):

        super().__init__(id_servicio, nombre, precio_hora)

        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ErrorServicio("La capacidad debe ser un entero positivo.")

        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def validar_parametros(self, horas: float) -> bool:
        if horas <= 0 or horas > self.MAX_HORAS:
            raise ErrorDisponibilidad(
                f"ReservaSala: las horas deben estar entre 1 y {self.MAX_HORAS}.")
        return True

    def descripcion(self) -> str:
        return (f"Sala de Conferencias | Capacidad: {self._capacidad} personas "
                f"| Precio/hora: ${self._precio_hora:,.0f} COP")


# ======================================
# ALQUILER EQUIPO
# ======================================
class AlquilerEquipo(Servicio):

    TIPOS_VALIDOS = {"laptop", "proyector", "camara", "tablet"}

    def __init__(self, id_servicio: str, nombre: str,
                 precio_hora: float, tipo_equipo: str, unidades: int):

        super().__init__(id_servicio, nombre, precio_hora)

        if tipo_equipo.lower() not in self.TIPOS_VALIDOS:
            raise ErrorServicio(
                f"Tipo de equipo inválido: '{tipo_equipo}'. "
                f"Válidos: {self.TIPOS_VALIDOS}")

        if not isinstance(unidades, int) or unidades <= 0:
            raise ErrorServicio("Las unidades deben ser un entero positivo.")

        self._tipo_equipo = tipo_equipo.lower()
        self._unidades    = unidades

    def validar_parametros(self, horas: float) -> bool:
        if horas <= 0:
            raise ErrorDisponibilidad("AlquilerEquipo: las horas deben ser positivas.")
        if self._unidades == 0:
            raise ErrorDisponibilidad("No hay unidades disponibles para alquilar.")
        return True

    def descripcion(self) -> str:
        return (f"Alquiler {self._tipo_equipo.capitalize()} "
                f"| Unidades: {self._unidades} "
                f"| Precio/hora: ${self._precio_hora:,.0f} COP")


# ======================================
# ASESORÍA ESPECIALIZADA
# ======================================
class AsesoriaEspecializada(Servicio):

    NIVELES      = {"basico", "intermedio", "avanzado"}
    MAX_SESIONES = 20

    def __init__(self, id_servicio: str, nombre: str,
                 precio_hora: float, especialidad: str, nivel: str):

        super().__init__(id_servicio, nombre, precio_hora)

        if not especialidad or len(especialidad.strip()) < 3:
            raise ErrorServicio("La especialidad debe tener al menos 3 caracteres.")

        if nivel.lower() not in self.NIVELES:
            raise ErrorServicio(
                f"Nivel inválido: '{nivel}'. Válidos: {self.NIVELES}")

        self._especialidad = especialidad.strip()
        self._nivel        = nivel.lower()

    def validar_parametros(self, horas: float) -> bool:
        if horas <= 0 or horas > self.MAX_SESIONES:
            raise ErrorDisponibilidad(
                f"Asesoria: máximo {self.MAX_SESIONES} sesiones.")
        return True

    def descripcion(self) -> str:
        return (f"Asesoría {self._especialidad.capitalize()} "
                f"| Nivel: {self._nivel} "
                f"| Precio/sesión: ${self._precio_hora:,.0f} COP")


# ======================================
# GESTOR DEL SISTEMA
# ======================================
class GestorSistema:

    def __init__(self):
        pass