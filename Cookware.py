from Container import Container
from HotStove import HotStove
from config import GRAY
from ObjectsID import ObjectsID

class Cookware(Container):
    def __init__(self, pos, shape,crate=None,type_id = ObjectsID.COOKWARE):
        super().__init__(pos, shape,crate,type_id)
        self.isWarm = False
        self.full = False

    def isOnStove(self, map):
        for obj in map.objects:
            if isinstance(obj, HotStove):
                if obj.pos == self.pos:
                    return True
        return False

    def draw(self, screen):
            super().draw(screen) 
            if self.isFull():
                self.addSoup(screen)
            elif self.isEmpty():
                self.clearSoup(screen,GRAY)

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    
    def interact(self, map):
        return super().interact(map)

    
    def add_ingredient(self, item):
        return super().add_ingredient(item)
    
    def isFull(self):
        return super().isFull()

    def addSoup(self, screen):
        return super().addSoup(screen)
    
    def isDropable(self, new_pos, map):
        return super().isDropable(new_pos, map)
    
    def cooking(self,map):
        if self.isOnStove(map):  
            if self.isFull():
            
                self.isWarm = True
                print("Le pot a cuit miam :)")
            else:
                print("Pas assez d\'ingrédient")
                print(self.ingredients)
        else:
            print("Le pot n\'est pas au dessus du feu")

    def clearSoup(self, screen, bg):
        return super().clearSoup(screen, bg)
    
    def getState(self):
        return super().getState(self) + [self.isWarm]