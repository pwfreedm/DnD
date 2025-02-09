from flask import Flask, render_template, request
from sqlalchemy import select, exists, func
from db import db
from model import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dnd.db'

db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['hp']:
            add_character(request.form)

        elif request.form['type']:
            add_item(request.form)
        
    return render_template('index.html')

def add_character (form):
    char = Character(form['name'].title(), form['hp'], form['weight'])
    db.session.add(char)
    db.session.commit()

def add_item (form):

    item = Item(0, form['name'], form['weight'], form['type'])

    if item.type == 'armor':
        item.base_ac = form['ac']
        
    elif item.type == 'weapon':
        item.hit_bonus = form['hit_bonus']
        item.dmg_bonus = form['dmg_bonus']
    
    else:
        item.quantity = form['quantity']
    #TODO: how to make sure this properly links up with Inventory
    # probably just end up making the form auto-include the character name?


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        
    app.run(debug=True)