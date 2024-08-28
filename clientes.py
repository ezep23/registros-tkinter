from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Clientes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="grey", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=500, height=110)
    
        titulo = tk.Label(self, text="Clientes", bg="black", fg="white", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=5, width=490, height=100)