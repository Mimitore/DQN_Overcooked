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
        # couper visuellement l'oignon
    
    def cooked(self):
        self.isCooked = True

    def draw(self, screen):
            super().draw(screen) 

    def isDropable(self, new_pos, interactables):
        return super().isDropable(new_pos,interactables)
