import tkinter as tk
from tkinter import ttk


class yes_window(tk.Tk,):
    def __init__(self):
        super().__init__()

        self.title("New Window")
        self.label = tk.Label(self, text="Si")
        self.label.pack()