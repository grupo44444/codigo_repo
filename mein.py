import tkinter as tk

ventana = tk.Tk()

palabra= tk.StringVar(ventana)
entrada= tk.StringVar(ventana)

ventana.geometry("600x600")
ventana.configure(background ="black")
ventana.title("hola compañeros")

def modificar():
    palabra.set("vamos con toda   "+ entrada.get())
tk.Button(
    ventana,
    text = "escribe tu nombre en el ultimo recuadro \n entonces oprime este boton luego y mira un pequeño mensaje",
    font = ("arial", 14),
    bg = "#00a8e8",
    fg = "white",
    command=modificar, 
    justify= "center"
).pack(
    fill = tk.BOTH,
    expand = True,
)

tk.Label(
    ventana,
    font = ("arial",14),
    text = "ey",
    textvariable= palabra,
    bg = "black",
    fg = "white",
    justify= "center",
).pack(
    fill = tk.BOTH,
    expand = True,
)

tk.Entry(
    font = ("arial", 14),
    bg = "black",
    fg = "white",
    justify= "center",
    textvariable= entrada,
).pack(
    fill = tk.BOTH,
    expand = True,
)


ventana.mainloop()
