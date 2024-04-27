import pygame
from GameObject import GameObject

from config import GRAY,BLACK,WHITE,ONION

class Item(GameObject):
    def __init__(self, pos, shape,type_id):
        super().__init__(type_id)
        self.pos = pos
        self.shape = shape

    def getPos(self):
        return self.pos
    
    def setPos(self,pos):
        self.pos = pos

    def update_position(self, player_x, player_y):
        self.pos = (player_x , player_y)

    def interact(self, map):
        """ Méthode pour gérer l'interaction d'un joueur avec l'item """
        if map.player.is_facing(self):
            map.player.take_item(self)
            print(f"Le joueur {map.player} interagit avec l'item à la position {self.pos}.")

    def draw(self, screen):
        if self.shape == "onion":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, ONION, center, 10)  
            pygame.draw.circle(screen, BLACK, center, 10,3)  
        
        elif self.shape == "pot":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, GRAY, center, 15)  
            pygame.draw.circle(screen, BLACK, center, 15,3) 
    
    def isDropable(self, new_pos, map):
            dropable = ["drop"]
            from InteractionManager import InteractionManager
            for obj in map.objects:
                if obj.pos == new_pos:
                    dropable.append(InteractionManager().process_interaction(self, obj,map))

            # Ici on gère les priorités si jamais 2 interactions sont possibles    
            if "del" in dropable:
                return 'del'
            elif "keep" in dropable:
                return "keep"
            return "drop"
    
    def getState(self):
        return super().getState(self) + [self.pos]