from CookingStation import CookingStation
import pygame
from config import WHITE,BLACK,GRAY
from ObjectsID import ObjectsID

class ServiceStation(CookingStation):
    def __init__(self, pos, shape):
        super().__init__(pos, shape,ObjectsID.SERVICE_STATION)


    def draw(self, screen):
        super().draw(screen)
        if self.shape == "service":
            pygame.draw.rect(screen, GRAY, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

    
    def checkPlate(self,plate):
        if plate.isFull():
            return True
        else:
            return False

    def getState(self):
        return super().getState()
    