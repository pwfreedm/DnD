from inventory import Item, Inventory

class Character:
    def __init__ (self, name: str):
        self._name = name
        self._inventory = Inventory()
