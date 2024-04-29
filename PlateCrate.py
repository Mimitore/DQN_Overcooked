from CookingStation import CookingStation
from Player import Player
from Container import Container
from config import WHITE,BLACK,GRAY
import pygame
from ObjectsID import ObjectsID

class PlateCrate(CookingStation):
    def __init__(self,pos,shape):
        super().__init__(pos,shape, ObjectsID.PLATE_CRATE)
       

    def draw(self, screen):
            super().draw(screen) 

            pygame.draw.rect(screen, GRAY,pygame.Rect(self.pos[0], self.pos[1], 50, 50))
            center = (self.pos[0] + 25, self.pos[1] + 25)

            pygame.draw.circle(screen, WHITE, center, 25)  
            pygame.draw.circle(screen, BLACK, center, 25,3)  
            pygame.draw.circle(screen, BLACK, center, 20,1) 

    def checkBlocked(self, map):
        return super().checkBlocked(map)
    

    def interact(self, map):
        super().interact(map)
        if not map.isAddable(Container(self.pos,"plate",self),map.objects, ObjectsID.PLATE):
            print("impossible d'ajouter une assiette")
            return
        if map.player.is_facing(self):
            if not self.is_blocked:
                if map.player.held_item is None:
                    new_item = Container(self.pos,"plate",self)
                    map.player.take_item(new_item)
                    map.add_object(new_item)
                    print(f"Le joueur a pris un {new_item} de la caisse.")
                else:
                    print(f"Le joueur tient déjà un {map.player.held_item}.")
            
            else:
                print("Un objet bloque la caisse, impossible de prendre un item.")
         
    def getState(self):
        return super().getState()