from CookingStation import CookingStation
from Vegetable import Vegetable
import pygame

class CuttingBoard(CookingStation):
    def __init__(self,pos):
        super().__init__(pos,"cuttingboard")
        self.item = None
    
    def place_item(self, item):
        self.item = item

    def cut_item(self):
        if isinstance(self.item, Vegetable):  
            self.item.cut()
            print(f"{self.item} a été cut")
        else:
            print("L'item sur la cuttingboard n'est pas de type Vegetable")

    def draw(self, screen):
            super().draw(screen) 

