from Item import Item
import pygame
from config import WHITE, BLACK,GRAY,ONION
from ObjectsID import ObjectsID

class Container(Item):
    def __init__(self, pos, shape,crate, type_id = ObjectsID.PLATE):
        super().__init__(pos, shape,type_id)
        self.ingredients = []
        self.full = False
        self.crate = crate

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    

    def draw(self, screen):
        super().draw(screen)
        if self.shape == "plate":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, WHITE, center, 25)  
            pygame.draw.circle(screen, BLACK, center, 25,3)  
            pygame.draw.circle(screen, BLACK, center, 20,1) 
        if self.isFull():
            self.addSoup(screen)
            
    def addSoup(self,screen):
        center = (self.pos[0] + 25, self.pos[1] + 25)
        pygame.draw.circle(screen,ONION,center,10)

    def add_ingredient(self,item):
        self.ingredients.append(item)

    def isDropable(self, new_pos, map):
        return super().isDropable(new_pos, map)

    def isFull(self):
        if len(self.ingredients)==2:
            self.full = True
            return True
        return False
    
    def isEmpty(self):
        if len(self.ingredients)==0:
            return True
        
        return False
    
    def transfer_ingredients_to(self, container):
        """Transfère tous les ingrédients de ce conteneur à un autre."""
        for ingredient in self.ingredients:
            container.add_ingredient(ingredient)
        self.ingredients.clear() 


    def clearSoup(self, screen,bg):
        if not self.full:
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, bg, center, 10)


    def getState(self):
        return super().getState() + [self.full]