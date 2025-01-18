import tkinter as tk
from model import InternalState

dm_bg = "#36393e"
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
        self.frame = tk.Frame(self.root, 
                              bg=dm_bg, 
                              width=1920, 
                              height=1080)
        self.canvases: list[CharacterPanel] = []

        self.frame.grid()
        self.draw_interface()
        self.root.title(name)

    def new_char_panel(self):
        self.canvases.append(CharacterPanel())
        self.canvases[len(self.canvases) - 1].grid(columnspan=5, rowspan=5, column=0, row=0)
        print("Button clicked")

    def create_button (self, text: str, command) -> tk.Button:
        return tk.Button(self.root, 
                        text=text, 
                        command=command,
                        bg=dm_bg,
                        fg=light_grey,
                        borderwidth=0)
        

    def draw_interface (self):
       add_menu = self.create_button('+', self.new_char_panel)
       add_menu.place(anchor='se',relx=0.996, rely=0.995)

class CharacterPanel (ResizingCanvas):
    def __init__ (self, root):
        self._canvas = ResizingCanvas(root, bg=light_grey, width=200, height=1000, highlightborder=0)
        self._canvas.addtag_all("window_resize")
