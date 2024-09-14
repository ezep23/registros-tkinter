import time
import tkinter as tk

root = tk.Tk()

root.title("Inventario")
root.geometry("800x600")
root.resizable(False, False)

#Intentar meterlo en clases
menu = tk.Frame(root)
menu.configure(width=800, height=600, bg="blue")


titulo = tk.Label(menu, text="INVENTARIO")
titulo.pack()

textoHora = tk.Label(menu)
textoHora.pack()

def actualizarHora():
    textoHora.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, actualizarHora)


actualizarHora()
menu.pack()
root.mainloop()