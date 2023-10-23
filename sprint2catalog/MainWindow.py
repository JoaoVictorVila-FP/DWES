from io import BytesIO
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
from detail_window import DetailWindow
from Cell import Cell

class Mainwindow(tk.Tk):
    

    
    # Call detail_window
    def on_button_clicked(self, t):
        r = DetailWindow(t.image_tk, t.title, t.desc)
        r.mainloop()
        
    #Load image into variable
    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        return img

    
        
    #Detail window main code
    def __init__(self, json_data):
        super().__init__()
        
        root = self
        
        
        
        #Menu
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Acerca de",
            command= show_messagebox)

        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        root.config(menu=barra_menus)
        
        
    
        #create cells
        self.cells = []
        
        data = json_data
    
        
          
        x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2
        y = (root.winfo_screenheight() - root.winfo_reqheight())/2
        root.geometry(f"+{int(x)}+{int(y)}")
        
        
       
        for x in range(len(data)):
            
            name = data[x].get("name")
            description = data[x].get("description")
            url = data[x].get("image_url")
            
            img = self.load_image_from_url(url)
                
            self.cells.append(Cell(name,description, img))
            
        #Print images and titles

        for i, cell in enumerate(self.cells):
            label = ttk.Label(self, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
            
            
    
def show_messagebox():
    messagebox.showinfo("Message", "Escuchas mi musica en www.joaovictorvila.design")    
    

    
    
