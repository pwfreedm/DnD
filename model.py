from db import DB_Base, db, count_rows
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
import json


class Character(DB_Base):
    __tablename__ = 'characters'

    name: Mapped[str] = mapped_column(primary_key=True)
    max_life: Mapped[int] = mapped_column()
    carry_weight: Mapped[int] = mapped_column()

    def __init__ (self, name: str, life, weight):
        self.name = name
        self.max_life = life
        self.carry_weight = weight

    def __repr__ (self):
        return f'{{ "name":"{self.name}", "max_life":{self.max_life}, "carry_weight":{self.carry_weight} }}'
    

class Weapon (DB_Base):
    __tablename__ = 'weapons'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(ForeignKey("characters.name"), nullable=False)
    name: Mapped[str] = mapped_column()
    weight: Mapped[int] = mapped_column()
    hit_bonus: Mapped[int] = mapped_column()
    dmg_bonus: Mapped[int] = mapped_column()

    def __init__ (self, name, owner, weight, hit_bonus, dmg_bonus):
        self.id = count_rows(Weapon)
        self.owner = owner
        self.name = name
        self.weight = weight 
        self.hit_bonus = hit_bonus
        self.dmg_bonus = dmg_bonus

    def __repr__ (self):
        return f'{{ "id":{self.id}, "owner:":"{self.owner}", "name":"{self.name}", "weight":{self.weight}, "hit_bonus":{self.hit_bonus}, "dmg_bonus":{self.dmg_bonus} }}'
    

class Armor (DB_Base):
    __tablename__ = 'armors'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(ForeignKey("characters.name"), nullable=False)
    name: Mapped[str] = mapped_column()
    weight: Mapped[int] = mapped_column()
    base_ac: Mapped[int] = mapped_column()

    def __init__ (self, name, owner, weight, base_ac):
        self.id = count_rows(Armor)
        self.owner = owner
        self.name = name
        self.weight = weight
        self.base_ac = base_ac

    def __repr__ (self):
        return f'{{ "id":{self.id}, "owner:":"{self.owner}", "name":"{self.name}", "weight":{self.weight}, "ac":{self.base_ac} }}'
    
class Item (DB_Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    owner: Mapped[str] = mapped_column(ForeignKey("characters.name"), nullable=False)
    name: Mapped[str] = mapped_column(unique=True)
    weight: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()

    def __init__ (self, name, owner, weight, quantity):
        self.id = count_rows(Item)
        self.owner = owner
        self.name = name
        self.weight = weight
        self.quantity = quantity

    def __repr__ (self):
        return f'{{ "id":{self.id}, "owner:":"{self.owner}", "name":"{self.name}", "weight":{self.weight}, "quantity":{self.quantity} }}'
    
def inventory_json (name: str):
    armors = db.session.execute(select(Armor).where(Armor.owner == name)).scalars()
    weapons = db.session.execute(select(Weapon).where(Weapon.owner == name)).scalars()
    items = db.session.execute(select(Item).where(Item.owner == name)).scalars()

    #TODO: integrate json header so that json dumps can be easily specified
