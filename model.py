from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Character(db.Model):
    name: Mapped[str] = mapped_column(primary_key=True)
    max_life: Mapped[int] = mapped_column()
    cur_life: Mapped[int] = mapped_column()
    carry_weight: Mapped[int] = mapped_column()

    def __init__ (self, name, life, weight):
        self.name = name
        self.max_life = life
        self.cur_life = life
        self.carry_weight = weight

class Item (db.Model):
    #TODO: add a method to this class that checks if an item that currently exists in the db is identical to one passed in (except ID)
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(unique=True)
    weight: Mapped[int] = mapped_column()
    #TODO: limit type to one of ['item', 'armor', 'weapon']
    type: Mapped[str] = mapped_column(nullable=False)
    hit_bonus: Mapped[int] = mapped_column()
    dmg_bonus: Mapped[int] = mapped_column()
    base_ac: Mapped[int] = mapped_column()

    def __init__ (self, id, name, weight, type, hit_bonus = None, dmg_bonus = None, base_ac = None):
        self.id = id
        self.name = name
        self.weight = weight
        self.type = type
        self.hit_bonus = hit_bonus
        self.dmg_bonus = dmg_bonus
        self.base_ac = base_ac

class Inventory(db.Model):
    #transaction id to optimize inventory updates
    t_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(None, ForeignKey('character.name'))
    item_id: Mapped[int] = mapped_column(None, ForeignKey('item.id'))
    quantity: Mapped[int] = mapped_column()