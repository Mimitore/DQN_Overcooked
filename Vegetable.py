import pygame
from Item import Item

from config import GRAY,BLACK,WHITE,ONION

class Vegetable(Item):
    def __init__(self, pos, shape, vege, state="non-cut"):
        super().__init__(pos, shape) 
        self.item_type = vege # "oignon", "champignon" ou "tomate"
        self.state = "non-cut"

    def getPos(self):
        return self.pos
    
    def setPos(self,pos):
        self.pos = pos

    def update_position(self, player_x, player_y):
        self.pos = (player_x , player_y)
    
    def cut(self):
        self.state = "cut"
        print("Vegetable coupé !")


    def interact(self, player):
        super().interact(player)

    def draw(self, screen):
        super().draw(screen)
    