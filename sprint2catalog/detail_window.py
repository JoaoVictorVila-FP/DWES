import tkinter as tk
from tkinter import Label, ttk
from PIL import Image, ImageTk

from Cell import Cell
from PIL import Image



    
    
class DetailWindow:
        
        
    def __init__(self, i, t,d):
        
        
        root = tk.Toplevel()

        x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2
        y = (root.winfo_screenheight() - root.winfo_reqheight())/2
        root.geometry(f"+{int(x)}+{int(y)}")
        root.title("Detailwindow " + t)
        
        print("Initiated detailwindow " + t)


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