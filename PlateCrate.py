from CookingStation import CookingStation
from Player import Player
from Container import Container
from config import WHITE,BLACK,GRAY
import pygame
class PlateCrate(CookingStation):
    def __init__(self,pos,shape):
        super().__init__(pos,shape)
        self.items = []


    def draw(self, screen):
            super().draw(screen) 
            for item in self.items:
                item.draw(screen)

            pygame.draw.rect(screen, GRAY,pygame.Rect(self.pos[0], self.pos[1], 50, 50))
            center = (self.pos[0] + 25, self.pos[1] + 25)

            pygame.draw.circle(screen, WHITE, center, 25)  
            pygame.draw.circle(screen, BLACK, center, 25,3)  
            pygame.draw.circle(screen, BLACK, center, 20,1) 

    def checkBlocked(self, player):
        return super().checkBlocked(player)
    
    def removeItem(self,item):
        if item in self.items:
            self.items.remove(item)


    def interact(self, player):
        super().interact(player)
        if player.is_facing(self):
            if not self.is_blocked:
                if player.held_item is None:
                    new_item = Container(self.pos,"plate")
                    player.take_item(new_item)
                    self.items.append(new_item)
                    player.interactables.append(new_item)
                    print(f"Le joueur a pris un {new_item} de la caisse.")
                else:
                    print(f"Le joueur tient déjà un {player.held_item}.")
            
            else:
                print("Un objet bloque la caisse, impossible de prendre un item.")
         
