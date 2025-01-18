from character import Character
from inventory import Inventory, Item


    
class InternalState():
    _self = None

    def __new__ (cls):
        if cls._self is None: 
            cls._self = super().__new__(cls)
        return cls._self
    
    def __init__ (self):
        self._characters: list[Character] = []
    
    def add_charcter(self, name: str, life: int):
        self._characters.append(Character(name, life))
    
    def remove_character(self, name: str):
        for c in self._characters:
            if c._name == name: 
                self._characters.remove(c)
    
    def get_character (self, name: str) -> Character:
        for c in self._characters: 
            if c._name == name: 
                return c
        