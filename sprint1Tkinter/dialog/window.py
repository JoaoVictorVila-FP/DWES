import tkinter as tk
from tkinter import ttk
from yes_window import yes_window
from no_window import no_window

class Mainwindow(tk.Tk):
    def on_buttonyes_click(self):
        a = yes_window()
        a.mainloop()

        
        
    def on_buttonno_click(self):
        a = no_window()
        a.mainloop()
    
    

    def __init__(self):
        super().__init__()
        
        self.label = tk.Label(self, text="Hello, tkinter!")
        self.label.pack()
        

        self.button1 = ttk.Button(self, text="Si", command=self.on_buttonyes_click)
        self.button1.pack()
        
        
        self.button2 = ttk.Button(self, text="No", command=self.on_buttonno_click)
        self.button2.pack()

        
        
        
        
if __name__ == "__main__":
    root = Mainwindow()
    root.mainloop()