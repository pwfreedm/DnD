from markupsafe import escape
import flask as fl
from db import db
from model import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = fl.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dnd.db'

db.init_app(app)


@app.route("/")
def index():
    return fl.render_template('index.html')

@app.post("/acs")
def add_character():
    return index()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)