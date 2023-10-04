import tkinter as tk
from tkinter import ttk

class Mainwindow(tk.Tk):
    def on_button_click(self):
        pass

    def __init__(self):
        super().__init__()

        self.button = ttk.Button(self, text="Realizar accion", command=self.on_button_click)
        self.button.pack()

        self.label = tk.Label(self, text="Hello, tkinter!")
        self.label.pack()
        
        
        
if __name__ == "__main__":
    root = Mainwindow()
    root.mainloop()