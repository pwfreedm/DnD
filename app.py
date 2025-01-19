from controller import Controller
from markupsafe import escape
import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def index():
    return fl.render_template('index.html')