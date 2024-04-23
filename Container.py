from Item import Item
import pygame
from config import WHITE, BLACK,GRAY

class Container(Item):
    def __init__(self, pos, shape):
        super().__init__(pos, shape)
        self.ingredients = []

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    

    def draw(self, screen):
        super().draw(screen)
        if self.shape == "plate":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, WHITE, center, 25)  
            pygame.draw.circle(screen, BLACK, center, 25,3)  
            pygame.draw.circle(screen, BLACK, center, 20,1) 

    def add_ingredient(self,item):
        self.ingredients.append(item)

    def isDropable(self, new_pos, interactables):
        return super().isDropable(new_pos, interactables)

    