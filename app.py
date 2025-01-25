from flask import Flask, render_template, request
from db import db
from model import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text, select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dnd.db'

db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        char = Character(request.form['name'], request.form['hp'], request.form['weight'])
        db.session.add(char)
        db.session.commit()

        print(db.session.query(Character).all())
        
        #DEBUG CODE PLEASE REMOVE
        with app.app_context():
            db.drop_all()
            db.create_all()
        
    return render_template('index.html')

def add_character():
    print("Form Submitted. ")
    return index()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)