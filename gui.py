import flask as fl
from model import InternalState

dm_bg = "#36393e"
light_grey = "#D3D3D3"
text_font = ("Righteous", 12)

class GUI:
    app = fl.Flask(__name__)

    def __init__ (self, name: str):
        pass
    
    @app.route("/")
    def display_msg(self):
        return "<p>General Kenobi!</p>"