
#represents one item in dnd
class Item: 
    def __init__ (self, name: str, weight: int, attrs: list[str] = []):
        self._name = name
        self._weight = weight
        self._attrs = attrs

    def weight (self) -> int: 
        return self._weight
    
    def name (self) -> str: 
        return self._name
    
    def attributes (self) -> list[str]:
        return self._attrs
    
    def __eq__ (self, o) -> bool:
        if not isinstance(o, Item): return False
        if self._name != o._name: return False
        if self._weight != o._weight: return False
        if self._attrs != o._attrs: return False
        return True
    
    def __neq__ (self, o) -> bool: 
        return not self == o

#represents an inventory in dnd
class Inventory: 
    def __init__ (self, limit: int = 0, items: list[Item] = []):
        self._items = items
        self._limit = limit
        self._cur_weight = 0
    
    def add_item(self, item: Item):
        self._cur_weight += item.weight()
        self._items.append(item)
    
    def remove_item (self, item: Item):
        self._cur_weight -= item.weight()
        self._items.remove(item)
    

