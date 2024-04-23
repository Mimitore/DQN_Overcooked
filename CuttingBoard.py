from CookingStation import CookingStation
import pygame

class CuttingBoard(CookingStation):
    def __init__(self,pos):
        
        
        super().__init__(pos,"cuttingboard")
    
    def draw(self, screen):
            super().draw(screen) 

