import tkinter as tk
from tkinter import Label, ttk
from PIL import Image, ImageTk

from Cell import Cell
from PIL import Image



    
    
class DetailWindow:
        
        
    def __init__(self, i, t,d):
        
        
        root = tk.Toplevel()

        
        print("Initiated detailwindow")


#Create title
        
        label_text = t
        label = tk.Label(root, text=label_text)
        label.pack()



#Create image 
        
        img =i
        label = tk.Label(root, image=img)
        label.pack()
        
        
      #create description  
        label_text = d
        label = tk.Label(root, text=label_text)
        label.pack()

                    
        root.mainloop()