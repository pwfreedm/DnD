from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Character(db.Model):
    name: Mapped[str] = mapped_column(primary_key=True)
    max_life: Mapped[int] = mapped_column()
    cur_life: Mapped[int] = mapped_column()
    carry_weight: Mapped[int] = mapped_column()

class Item (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(unique=False)
    weight: Mapped[int] = mapped_column()
    item_type: Mapped[str] = mapped_column(nullable=False)
    __mapper_args__ = {'polymorphic_on': item_type}

class Weapon (Item):
    __mapper_args__ = {'polymorphic_identity': 'weapon'}
    id: Mapped[int] = mapped_column(None, ForeignKey('item.id'), primary_key=True)
    hit_bonus: Mapped[int] = mapped_column()
    dmg_bonus: Mapped[int] = mapped_column()

class Armor (Item):
    __mapper_args__ = {'polymorphic_identity': 'armor'}
    id: Mapped[int] = mapped_column(None, ForeignKey('item.id'), primary_key=True)
    base_ac: Mapped[int] = mapped_column()

class Inventory(db.Model):
    name: Mapped[str] = mapped_column(None, ForeignKey('character.name'), primary_key=True)
    item_id: Mapped[int] = mapped_column(None, ForeignKey('item.id'), unique=True)
    quantity: Mapped[int] = mapped_column()