from CookingStation import CookingStation
from Vegetable import Vegetable
from ObjectsID import ObjectsID

class CuttingBoard(CookingStation):
    def __init__(self,pos):
        super().__init__(pos,"cuttingboard",ObjectsID.CUTTING_BOARD)

    def cut_item(self):
        if isinstance(self.item, Vegetable):  
            self.item.cut()
            print(f"{self.item} a été cut")
        else:
            print("L'item sur la cuttingboard n'est pas de type Vegetable")

    def draw(self, screen):
            super().draw(screen) 

    def interact(self, map):
        super().interact(map)
        for obj in map.objects:
             if obj.pos == self.pos and obj!=self:
                self.item = obj
                break
             
    def get_state(self):
        return super().get_state(self)