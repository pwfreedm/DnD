from inventory import Item, Inventory

class Character:
    def __init__ (self, name: str, max_life: int):
        self._name = name
        self._inventory = Inventory()
        self._max_life = max_life
        self._life = max_life

    def take_damage(self, amount: int):
        self._life -= amount

    def heal(self, amount: int):
        self._life = min(self._max_life, self._life + amount)
    
    def level_up (self, extra_hp: int):
        self._max_life += extra_hp
        self._life += extra_hp
    
