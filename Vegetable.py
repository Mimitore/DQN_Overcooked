import pygame
from Item import Item

from config import GRAY,BLACK,WHITE,ONION

class Vegetable(Item):
    def __init__(self, pos, shape,crate):
        super().__init__(pos, shape) 
        self.isCut = False
        self.crate = crate
    
    def cut(self):
        self.isCut = True
        # coupêr visuellement l'oignon

    def draw(self, screen):
            super().draw(screen) 
    