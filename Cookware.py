from Container import Container
from HotStove import HotStove

class Cookware(Container):
    def __init__(self, pos, shape,crate=None):
        super().__init__(pos, shape,crate)
        self.isWarm = False
    
    def isOnStove(self, interactables):
        for obj in interactables:
            if isinstance(obj, HotStove):
                if obj.pos == self.pos:
                    return True
        return False

    def draw(self, screen):
            super().draw(screen) 

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    
    def interact(self, player):
        return super().interact(player)
    
    def draw(self, screen):
        return super().draw(screen)
    
    def add_ingredient(self, item):
        return super().add_ingredient(item)
    
    def isFull(self):
        return super().isFull()

    def isDropable(self, new_pos, interactables):
        return super().isDropable(new_pos, interactables)
    
    def cooking(self,interactables):
        if self.isOnStove(interactables):  
            if self.isFull():
            
                self.isWarm = True
                print("Le pot a cuit miam :)")
            else:
                print("Pas assez d\'ingrédient")
                print(self.ingredients)
        else:
            print("Le pot n\'est pas au dessus du feu")