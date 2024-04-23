import pygame


from config import GRAY,BLACK,WHITE,ONION

class Item:
    def __init__(self, pos,shape,state):
        super().__init__(pos,shape)
        state = self.state

    def getPos(self):
        return self.pos
    
    def setPos(self,pos):
        self.pos = pos

    def update_position(self, player_x, player_y):
        self.pos = (player_x , player_y)
       


    def interact(self, player):
        super().interact(player)

    def draw(self, screen):
        super().draw(screen)
    