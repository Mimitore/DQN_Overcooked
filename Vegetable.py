import pygame
from Item import Item
from Cookware import Cookware
from config import GRAY,BLACK,WHITE,ONION
from ObjectsID import ObjectsID

class Vegetable(Item):
    def __init__(self, pos, shape,crate,type_id = ObjectsID.ONION):
        super().__init__(pos, shape,type_id) 
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

    def isDropable(self, new_pos, map):
        return super().isDropable(new_pos,map)

    def getState(self):
        return super().getState(self) + [self.isCut]