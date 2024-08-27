from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class Container (tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=500, height=350)
        self.config(bg="#dddddd")
        self.widgets()
    
    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#dddddd")
        frame.pack(fill="both", expand=True)
        top_level.geometry("500x350")
        top_level.resizable(False, False)

    def clientes(self):
        self.show_frames(Clientes)

    def registros(self):
        self.show_frames(Registros)

    def widgets(self):
        frame1= tk.Frame(self, bg="#dddddd")
        frame1.pack()
        frame1.place(x=0, y=0, width=500, height=350)

        welcome_label = tk.Label(frame1, text="SISTEMA DE GESTIÓN", fg="black", bg="#dddddd", font="sans 20 bold")
        welcome_label.place(x=100, y=40)

        btnClientes = Button(frame1, bg="#000000", fg="white", text="Ir a clientes", command=self.clientes)
        btnClientes.place(x=130, y=110, width=240, height=60)

        btnRegistro = Button(frame1, bg="#000000", fg="white", text="Ir a registros", command=self.registros)
        btnRegistro.place(x=130, y=190, width=240, height=60)
        
        copyright_label = tk.Label(frame1, text="Creado por Ezequiel Pistone", bg="#dddddd", fg="black", font="sans 16 bold", anchor="center")
        copyright_label.place(x=105, y=290)