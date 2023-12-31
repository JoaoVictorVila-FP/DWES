import tkinter as tk
from PIL import Image,ImageTk

class Cell:
    
    #Variables
    def __init__(self,title,path,desc):
        self.title = title
        self.path = path
        self.image_tk = resize_image(self.path, 100, 100)
        self.desc = desc
        
        
        
#resize the image   
def resize_image(image_path, new_width, new_height):
    
    img = Image.open(image_path)
    
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    return ImageTk.PhotoImage(img)