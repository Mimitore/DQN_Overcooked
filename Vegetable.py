import pygame
from Item import Item

from config import GRAY,BLACK,WHITE,ONION

class Vegetable(Item):
    def __init__(self, pos, shape):
        super().__init__(pos, shape) 
        self.state = "non-cut"
    
    def cut(self):
        self.state = "cut"
        # coupêr visuellement l'oignon

    def draw(self, screen):
            super().draw(screen) 
    