import tkinter as tk
from tkinter import ttk

from Cell import Cell

class Mainwindow(tk.Tk):
    def on_button_clicked():
       message = "has hecho click en la celda" + Cell.title
       messagebox.showinfo("Informacion", message)


    def __init__(self, root):
        super().__init__()
        
        self.cells = [
            
            Cell("Edward Teach","data\unedited\BB.webp"),
            Cell("Bartholomew Roberts","data\unedited\BartholomewRoberts.jpg"),
            Cell("Captain Morgan","data\unedited\CaptainHenryMorgan1-802187d289ec4e2d9bf374fdd6b82160.jpg"),
            Cell("Benjamin Horningold","data\unedited\hornigold_1724_wikimedia.jpg"),
            Cell("Jack Rackham","data\unedited\Rackham,_Jack.jpg")
        ]
        
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image = cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=i, column= 0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_buttion_clicked(celda))
        
        
        
        
if __name__ == "__main__":
    root = Mainwindow()
    root.mainloop()