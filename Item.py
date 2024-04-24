import pygame


from config import GRAY,BLACK,WHITE,ONION

class Item:
    def __init__(self, pos, shape):
        self.pos = pos
        self.shape = shape

    def getPos(self):
        return self.pos
    
    def setPos(self,pos):
        self.pos = pos

    def update_position(self, player_x, player_y):
        self.pos = (player_x , player_y)
       


    def interact(self, player):
        """ Méthode pour gérer l'interaction d'un joueur avec l'item """
        if player.is_facing(self):
            player.take_item(self)
            print(f"Le joueur {player} interagit avec l'item à la position {self.pos}.")

    def draw(self, screen):
        if self.shape == "onion":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, ONION, center, 10)  
            pygame.draw.circle(screen, BLACK, center, 10,3)  
        
        elif self.shape == "pot":
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, GRAY, center, 10)  
            pygame.draw.circle(screen, BLACK, center, 10,3) 
    
    def isDropable(self, new_pos, interactables):
            dropable = ["drop"]
            from InteractionManager import InteractionManager
            for obj in interactables:
                if obj.pos == new_pos:
                    dropable.append(InteractionManager().process_interaction(self, obj,interactables))
                    
            if "del" in dropable:
                return 'del'
            elif "keep" in dropable:
                return "keep"
            return "drop"