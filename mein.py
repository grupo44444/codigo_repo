import tkinter as tk

from tkinter import (
    ttk,
    messagebox
)

from clientes import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reservas import Reserva


reservas_creadas = []


# ======================================
# CREAR RESERVA
# ======================================

def crear_reserva():

    try:

        nombre = entrada_nombre.get()

        cedula = entrada_cedula.get()

        correo = entrada_correo.get()

        cliente = Cliente(
            nombre,
            cedula,
            correo
        )

        tipo_servicio = combo_servicio.get()

        cantidad = int(
            entrada_cantidad.get()
        )

        if tipo_servicio == "Reserva Sala":

            servicio = ReservaSala(cantidad)

        elif tipo_servicio == "Alquiler Equipo":

            servicio = AlquilerEquipo(cantidad)

        else:

            servicio = AsesoriaEspecializada(
                cantidad
            )

        reserva = Reserva(
            cliente,
            servicio
        )

        reserva.confirmar()

        reservas_creadas.append(
            reserva
        )

        total = reserva.calcular_total(
            impuesto=0.19,
            descuento=5000
        )

        texto_resultado.config(

            text=

            f"RESERVA CREADA\n\n"

            f"Cliente: {cliente.nombre}\n"

            f"Servicio: {servicio.nombre}\n"

            f"Total: ${total}"

        )

    except Exception as error:

        messagebox.showerror(
            "ERROR",
            str(error)
        )


# ======================================
# PAGAR
# ======================================

def pagar_reserva():

    try:

        if reservas_creadas:

            reserva = reservas_creadas[-1]

            reserva.pagar()

            messagebox.showinfo(
                "PAGO",
                "Pago realizado"
            )

    except Exception as error:

        messagebox.showerror(
            "ERROR",
            str(error)
        )


# ======================================
# CANCELAR
# ======================================

def cancelar_reserva():

    try:

        if reservas_creadas:

            reserva = reservas_creadas[-1]

            reserva.cancelar()

            messagebox.showinfo(
                "CANCELADA",
                "Reserva cancelada"
            )

    except Exception as error:

        messagebox.showerror(
            "ERROR",
            str(error)
        )


# ======================================
# VENTANA
# ======================================

ventana = tk.Tk()

ventana.title(
    "Software FJ"
)

ventana.geometry(
    "600x500"
)


# ======================================
# NOMBRE
# ======================================

tk.Label(

    ventana,
    text="Nombre"

).pack()

entrada_nombre = tk.Entry(
    ventana
)

entrada_nombre.pack()


# ======================================
# CÉDULA
# ======================================

tk.Label(

    ventana,
    text="Cédula"

).pack()

entrada_cedula = tk.Entry(
    ventana
)

entrada_cedula.pack()


# ======================================
# CORREO
# ======================================

tk.Label(

    ventana,
    text="Correo"

).pack()

entrada_correo = tk.Entry(
    ventana
)

entrada_correo.pack()


# ======================================
# SERVICIO
# ======================================

tk.Label(

    ventana,
    text="Servicio"

).pack()

combo_servicio = ttk.Combobox(

    ventana,

    values=[

        "Reserva Sala",

        "Alquiler Equipo",

        "Asesoría"

    ]

)

combo_servicio.pack()


# ======================================
# CANTIDAD
# ======================================

tk.Label(

    ventana,
    text="Horas / Días / Sesiones"

).pack()

entrada_cantidad = tk.Entry(
    ventana
)

entrada_cantidad.pack()


# ======================================
# BOTONES
# ======================================

tk.Button(

    ventana,

    text="Crear Reserva",

    command=crear_reserva

).pack(pady=10)


tk.Button(

    ventana,

    text="Pagar Reserva",

    command=pagar_reserva

).pack(pady=10)


tk.Button(

    ventana,

    text="Cancelar Reserva",

    command=cancelar_reserva

).pack(pady=10)


# ======================================
# RESULTADO
# ======================================

texto_resultado = tk.Label(

    ventana,

    text="",

    justify="left"

)

texto_resultado.pack(pady=20)


ventana.mainloop()