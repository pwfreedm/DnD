from app import app
from db import *
from model import *

def commit_item(item: object):
    db.session.add(item)
    db.session.commit()

with app.app_context():
    db.drop_all()
    db.create_all()

    char = Character("Peter")
    commit_item(char)

    stats = Stats("Peter", 10, 10)
    commit_item(stats)

    char2 = Character("John")
    commit_item(char2)

    stats2 = Stats("John", 15, 15)
    commit_item(stats2)

    i1 = Item('torch', 'Peter', 0.1, 40)
    commit_item(i1)

    i2 = Item('tobacco pouch', 'Peter', 0.3, 1)
    commit_item(i2)

    w1 = Weapon('short sword', 'Peter', 6, 1, 1)
    commit_item(w1)

    w2 = Weapon('Bow', 'Peter', 5, 2, 3)
    commit_item(w2)

    a1 = Armor('Plate Mail', 'Peter', 25, 3)
    commit_item(a1)

    a2 = Armor('Leather', 'Peter', 5, 6)
    commit_item(a2)

    a3 = Armor('Leather', 'John', 5, 6)
    commit_item(a3)

    print(character_json("Peter"))  


