from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Registros(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()
    
    def widgets(self):
        
        frame1 = tk.Frame(self, bg="#d6d6d6", highlightbackground="gray", highlightthickness=1) 
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="Registros", bg="grey", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=5, width=1090, height=90)

