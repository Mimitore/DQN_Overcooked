import pygame
from Item import Item
from Cookware import Cookware
from config import GRAY,BLACK,WHITE,ONION

class Vegetable(Item):
    def __init__(self, pos, shape,crate):
        super().__init__(pos, shape) 
        self.isCut = False
        self.isCooked = False
        self.crate = crate
    
    def cut(self):
        self.isCut = True
        # coupêr visuellement l'oignon
    
    def cooked(self):
        self.isCooked = False

    def draw(self, screen):
            super().draw(screen) 

    def on_drop(self, new_pos, interactables):
        super().on_drop(new_pos,interactables)
        if self.isCut:
            for obj in interactables:
                if isinstance(obj, Cookware) and obj.pos == self.pos:
                    obj.add_ingredient(self)
                    return True  # Indique que le légume a été ajouté à un Cookware
        return False