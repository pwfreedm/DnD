from model import InternalState
from gui import GUI

class Controller: 
    _self = None

    #controller is singleton
    def __new__ (cls, window_name: str):
        if cls._self is None: 
            cls._self = super().__new__(cls)
        return cls._self
    
    def __init__ (self, window_name: str):
        self._gui = GUI(window_name)
        self._state = InternalState()

    def init_gui (self):
        self._gui.root.mainloop()
        

