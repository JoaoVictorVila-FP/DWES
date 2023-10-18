import tkinter as tk
from PIL import Image,ImageTk

class Cell:
    
    #Variables
    def __init__(self,title,desc,img):
        self.title = title
        self.image_tk = img
        self.desc = desc
        
        