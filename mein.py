"""
=============================================================
  Interfaz Gráfica — Sistema Software FJ
  Usa las clases definidas en sistema.py
=============================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox

from servicios import (
    Cliente,
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
    Reserva,
    GestorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorParametro,
    ErrorDisponibilidad
)

# Gestor global del sistema
gestor = GestorSistema()

# Contador para IDs automáticos
_contador = {"cliente": 1, "servicio": 1, "reserva": 1}

def _nuevo_id(tipo: str) -> str:
    id_gen = f"{tipo[0].upper()}{_contador[tipo]:03d}"
    _contador[tipo] += 1
    return id_gen

# Lista de reservas creadas en la sesion
reservas_creadas = []


# ======================================
# CREAR RESERVA
# ======================================
def crear_reserva():
    try:
        nombre       = entrada_nombre.get().strip()
        cedula       = entrada_cedula.get().strip()
        correo       = entrada_correo.get().strip()
        cantidad_str = entrada_cantidad.get().strip()

        if not nombre or not cedula or not correo or not cantidad_str:
            raise ErrorParametro("Todos los campos son obligatorios.")

        id_cliente = _nuevo_id("cliente")
        cliente = Cliente(id_cliente, nombre, correo, cedula)
        gestor._clientes[id_cliente] = cliente

        try:
            cantidad = float(cantidad_str)
        except ValueError:
            raise ErrorParametro(f"La cantidad debe ser un número. Recibido: '{cantidad_str}'")

        tipo_servicio = combo_servicio.get()
        if not tipo_servicio:
            raise ErrorParametro("Debe seleccionar un tipo de servicio.")

        id_servicio = _nuevo_id("servicio")

        if tipo_servicio == "Reserva Sala":
            servicio = ReservaSala(
                id_servicio,
                "Sala de Conferencias",
                precio_hora=80000,
                capacidad=20
            )
        elif tipo_servicio == "Alquiler Equipo":
            servicio = AlquilerEquipo(
                id_servicio,
                "Laptop HP ProBook",
                precio_hora=35000,
                tipo_equipo="laptop",
                unidades=5
            )
        else:
            servicio = AsesoriaEspecializada(
                id_servicio,
                "Asesoria Especializada",
                precio_hora=120000,
                especialidad="software",
                nivel="intermedio"
            )

        gestor._servicios[id_servicio] = servicio

        id_reserva = _nuevo_id("reserva")
        reserva = Reserva(id_reserva, cliente, servicio, cantidad, descuento=0.0)

        reserva.confirmar()
        reservas_creadas.append(reserva)

        total = reserva.costo_total

        texto_resultado.config(
            text=(
                f"✔ RESERVA CREADA\n\n"
                f"ID Reserva: {id_reserva}\n"
                f"Cliente:    {cliente.nombre}\n"
                f"Cédula:     {cedula}\n"
                f"Servicio:   {servicio.nombre}\n"
                f"Horas:      {cantidad}\n"
                f"Total:      ${total:,.2f} COP (IVA incluido)"
            )
        )

    except (ErrorCliente, ErrorServicio, ErrorReserva,
            ErrorParametro, ErrorDisponibilidad) as e:
        messagebox.showerror("Error del sistema", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))


# ======================================
# PAGAR
# ======================================
def pagar_reserva():
    try:
        if not reservas_creadas:
            messagebox.showwarning("Sin reservas", "No hay reservas activas.")
            return

        reserva = reservas_creadas[-1]
        reserva.procesar()

        messagebox.showinfo(
            "Pago realizado",
            f"Reserva {reserva.id_reserva} procesada exitosamente.\n"
            f"Total cobrado: ${reserva.costo_total:,.2f} COP"
        )
        texto_resultado.config(
            text=texto_resultado.cget("text") + f"\n\n► Estado: PROCESADA"
        )

    except ErrorReserva as e:
        messagebox.showerror("Error al procesar", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))


# ======================================
# CANCELAR
# ======================================
def cancelar_reserva():
    try:
        if not reservas_creadas:
            messagebox.showwarning("Sin reservas", "No hay reservas activas.")
            return

        reserva = reservas_creadas[-1]
        reserva.cancelar("Cancelado desde la interfaz gráfica")

        messagebox.showinfo(
            "Reserva cancelada",
            f"La reserva {reserva.id_reserva} fue cancelada."
        )
        texto_resultado.config(
            text=texto_resultado.cget("text") + f"\n\n✘ Estado: CANCELADA"
        )

    except ErrorReserva as e:
        messagebox.showerror("Error al cancelar", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))


# ======================================
# VENTANA PRINCIPAL
# ======================================
ventana = tk.Tk()
ventana.title("Software FJ — Sistema de Reservas")
ventana.geometry("600x560")
ventana.resizable(False, False)

frame = tk.Frame(ventana, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Sistema de Gestión Software FJ",
         font=("Arial", 14, "bold")).pack(pady=(0, 15))

tk.Label(frame, text="Nombre completo:", anchor="w").pack(fill="x")
entrada_nombre = tk.Entry(frame, width=50)
entrada_nombre.pack(pady=(0, 8))

tk.Label(frame, text="Cédula (teléfono):", anchor="w").pack(fill="x")
entrada_cedula = tk.Entry(frame, width=50)
entrada_cedula.pack(pady=(0, 8))

tk.Label(frame, text="Correo electrónico:", anchor="w").pack(fill="x")
entrada_correo = tk.Entry(frame, width=50)
entrada_correo.pack(pady=(0, 8))

tk.Label(frame, text="Tipo de servicio:", anchor="w").pack(fill="x")
combo_servicio = ttk.Combobox(
    frame,
    values=["Reserva Sala", "Alquiler Equipo", "Asesoría"],
    state="readonly",
    width=47
)
combo_servicio.pack(pady=(0, 8))

tk.Label(frame, text="Horas / Días / Sesiones:", anchor="w").pack(fill="x")
entrada_cantidad = tk.Entry(frame, width=50)
entrada_cantidad.pack(pady=(0, 15))

frame_botones = tk.Frame(frame)
frame_botones.pack(pady=5)

tk.Button(
    frame_botones, text="Crear Reserva",
    command=crear_reserva, width=18,
    bg="#1F4E79", fg="white", font=("Arial", 10, "bold")
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_botones, text="Pagar Reserva",
    command=pagar_reserva, width=18,
    bg="#1D6A3A", fg="white", font=("Arial", 10, "bold")
).grid(row=0, column=1, padx=5)

tk.Button(
    frame_botones, text="Cancelar Reserva",
    command=cancelar_reserva, width=18,
    bg="#C55A11", fg="white", font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=5)

tk.Label(frame, text="─" * 60, fg="#CCCCCC").pack(pady=(15, 5))

texto_resultado = tk.Label(
    frame, text="Complete el formulario y presione 'Crear Reserva'.",
    justify="left", anchor="w", wraplength=540,
    font=("Courier", 10)
)
texto_resultado.pack(fill="x", pady=5)

ventana.mainloop()