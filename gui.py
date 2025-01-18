from tkinter import *
# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event: Event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "resize" tag
        self.scale("resizable",0,0,wscale,hscale)


class GUI:
    def __init__ (self, name: str):
        self.root = Tk(className=name)
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)
        self.canvas = ResizingCanvas(self.frame, width=500, height=500, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.addtag_all("resizable")







def gui_setup () -> None:
    pass
