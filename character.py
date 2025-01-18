from inventory import Item, Inventory

class Character:
    def __init__ (self, name: str, max_life: int):
        self._name = name
        self._inventory = Inventory()
        self._max_life = max_life
        self._life = max_life

# Accessors ===================================================================
    def get_max_life (self) -> int:
        return self._max_life
    
    def get_cur_life (self) -> int:
        return self._life
    
    def get_inventory (self) -> Inventory: 
        return self._inventory
    
    def get_name (self) -> str: 
        return self._name

# Mutators ====================================================================
    def take_damage(self, amount: int):
        self._life -= amount

    def heal(self, amount: int):
        self._life = min(self._max_life, self._life + amount)
    
    def level_up (self, extra_hp: int):
        self._max_life += extra_hp
        self._life += extra_hp

    def change_name (self, new_name:str):
        self._name = new_name
    
    def set_max_life (self, new_life: int):
        self._max_life = new_life
    
