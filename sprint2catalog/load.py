import threading
import tkinter as tk

import requests

from MainWindow import Mainwindow

class LoadingWindow:
    
    
    
    
    def __init__(self,root):
        self.finished = False
        self.json_data =[]
        self.root = root
        self.root.title("Cargando....")
        
        
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        
    
        
        
        
        self.root.resizable(False, False)        
        self.label = tk.Label(self.root, text ="Cargando datos....", font =("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)
        
        label_bg_color = self.label.cget("bg")
        
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()
        
        self.progress = 0
        self.draw_progress_circle(self.progress)
        self.update_progress_circle()
        
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        
        
        self.check_thread()
        

        
        
     #Draw Circle   
        
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle= int(360 * (progress / 100))
        
        
        self.canvas.create_arc(10,10,35,35, 
                               start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
        
        
    #Update Circle
    def update_progress_circle(self):
        
        if self.progress < 100:
            self.progress += 10
        else:
            self.progress = 0
            
            
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)
        
    
    #Get the data from the github link
    def fetch_json_data(self):
       
        response = requests.get("https://raw.githubusercontent.com/JoaoVictorVila-FP/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True
            
    
    #Launch the mainwindow if possible
    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100,self.check_thread)
            
            
        
#Launch the main window      
def launch_main_window(json_data):

    app = Mainwindow(json_data)
    app.mainloop()
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        