import tkinter as tk
from tkinter import ttk
from detail_window import DetailWindow
from Cell import Cell

class Mainwindow(tk.Tk):
    
    # Call detail_window
    def on_button_clicked(self, t):
        r = DetailWindow(t.image_tk, t.title, t.desc)
        r.mainloop()
        
        
    #Detail window main code
    def __init__(self):
        super().__init__()
        
        #create cells

        self.cells = [
            Cell("Edward Teach", "data\\unedited\\BB.webp","Blackbeard, the infamous pirate of the Golden Age of Piracy, was known for his menacing appearance, with a black beard adorned with slow-burning fuses, and a reputation for ruthless plundering and terrorizing the high seas in the early 18th century."),
            Cell("Bartholomew Roberts", "data\\unedited\\BartholomewRoberts.jpg","Bartholomew Roberts, or Black Bart, was a feared 18th-century pirate captain known for his strategic brilliance, capturing over 400 ships during the Golden Age of Piracy."),
            Cell("Captain Morgan", "data\\unedited\\CaptainHenryMorgan1-802187d289ec4e2d9bf374fdd6b82160.jpg", "Captain Morgan, a legendary 17th-century privateer turned pirate, is celebrated for his swashbuckling adventures and association with the famous spiced rum brand that bears his name."),
            Cell("Benjamin Horningold", "data\\unedited\\hornigold_1724_wikimedia.jpg","Captain Benjamin Hornigold, an early 18th-century pirate, was notorious for his ever-changing allegiances and later, his pardon-seeking efforts in the Caribbean, a complex figure in pirate history."),
            Cell("Jack Rackham", "data\\unedited\\Rackham,_Jack.jpg","Calico Jack, aka John Rackham, was an 18th-century pirate known for his distinctive attire, including calico clothing. He sailed with infamous female pirates Anne Bonny and Mary Read.")
        ]
        
        #Print images and titles

        for i, cell in enumerate(self.cells):
            label = ttk.Label(self, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))

    
    
    
    
    
    
