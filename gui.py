import tkinter as tk
from character import *
# a subclass of Canvas for dealing with resizing of windows

def_background = "#36393e"
light_grey = "#D3D3D3"
text_font = ("Righteous", 12)
class ResizingCanvas(tk.Canvas):
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event: tk.Event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "resize" tag
        self.scale("window_resize",0,0,wscale,hscale)

class GUI:
    def __init__ (self, name: str):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.canvas = ResizingCanvas(self.frame, width=1920, height=1080, background=def_background, highlightthickness=0)

        self.canvas.grid()
        self.frame.grid()
        self.draw_interface()
        self.root.title(name)
        self.canvas.addtag_all("window_resize")

    def add_character(self):
        print("Button clicked")

    def create_button (self, text: str, command) -> tk.Button:
        return tk.Button(self.root, 
                        text=text, 
                        command=command,
                        bg=def_background,
                        fg=light_grey,
                        borderwidth=0)
        

    def draw_interface (self):
       add_menu = self.create_button('+', self.add_character)
       add_menu.grid(row=5, column=5)

