from dataclasses import dataclass
from typing import List
from db import db
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

name_len: int = 50 
item_len: int = 100

@dataclass
class Stats (db.Model):
    __tablename__ = 'stats'

    owner: str = db.Column(db.String(name_len), ForeignKey("character.name"), primary_key=True)
    max_hp: int = db.Column(db.Integer)
    carry_weight: int = db.Column(db.Integer)

    def __init__ (self, name, max_hp, carry_weight):
        self.owner = name
        self.max_hp = max_hp
        self.carry_weight = carry_weight
@dataclass
class Weapon (db.Model):
    __tablename__ = 'weapon'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner: str = db.Column(db.String(name_len), ForeignKey("character.name"), nullable=False)
    name: str = db.Column(db.String(item_len))
    weight: int = db.Column(db.Integer)
    hit_bonus: int = db.Column(db.Integer)
    dmg_bonus: int = db.Column(db.Integer)

    def __init__ (self, name, owner, weight, hit_bonus, dmg_bonus):
        self.owner = owner
        self.name = name
        self.weight = weight 
        self.hit_bonus = hit_bonus
        self.dmg_bonus = dmg_bonus
    
@dataclass
class Armor (db.Model):
    __tablename__ = 'armor'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    owner: str = db.Column(db.String(name_len), ForeignKey("character.name"), nullable=False)
    name: str = db.Column(db.String(item_len))
    weight: int = db.Column(db.Integer)
    base_ac: int = db.Column(db.Integer)

    def __init__ (self, name, owner, weight, base_ac):
        self.owner = owner
        self.name = name
        self.weight = weight
        self.base_ac = base_ac
@dataclass    
class Item (db.Model):
    __tablename__ = 'item'

    id: int = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    owner: str = db.Column(db.String(name_len), ForeignKey("character.name"), nullable=False)
    name: str = db.Column(db.String(item_len))
    weight: int = db.Column(db.Numeric(2,2))
    quantity: int = db.Column(db.Integer)

    def __init__ (self, name, owner, weight, quantity):
        self.owner = owner
        self.name = name
        self.weight = weight
        self.quantity = quantity

@dataclass
class Character(db.Model):
    __tablename__ = 'character'
    __allow_unmapped__ = True #required to get relationships and jsonify to work right

    name: str = db.Column(db.String(name_len), primary_key=True)

    stats: Stats = db.relationship(Stats)
    armors: List[Armor] = db.relationship(Armor)
    weapons: List[Weapon] = db.relationship(Weapon)
    items: List[Item] = db.relationship(Item)

    def __init__ (self, name: str):
        self.name = name
    
def character_json (name: str):
    char = Character.query.where(Character.name == name).scalar()
    return jsonify({name: char})

def party_json ():
    return jsonify({'Party': [{char.name: char} for char in Character.query.all()]})
