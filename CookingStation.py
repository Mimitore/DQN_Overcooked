import pygame
from config import GRAY,BLACK,WHITE,ONION
from GameObject import GameObject

class CookingStation(GameObject):
    def __init__(self, pos, shape,type_id):
        super().__init__(type_id) 
        self.pos = pos
        self.shape = shape
        self.is_blocked = False
        self.item = None
        self.last_check_time = pygame.time.get_ticks()

    def getPos(self):
        return self.pos
        
    def setPos(self,pos):
        self.pos = pos    

    def checkBlocked(self, map):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_check_time >400:
            self.last_check_time = current_time
            self.is_blocked = False
            self.item = None
            for obj in map.objects:
                if obj.pos == self.pos and obj != self:
                    self.item = obj
                    self.is_blocked = True
                    print(f"{self} is blocked by {obj}")
                    break
            if not self.is_blocked:
                print(f"{self} is not blocked")

    def interact(self, map):
        """ Méthode pour gérer l'interaction d'un joueur avec la station """
        self.checkBlocked(map)
        if map.player.is_facing(self):
            print(f"Le joueur {map.player} interagit avec la station à la position {self.pos}.")


    def draw(self, screen):
        if self.shape == "hotstove":
            pygame.draw.rect(screen, WHITE, pygame.Rect(self.pos[0], self.pos[1], 50, 50))
            center = (self.pos[0] + 25, self.pos[1] + 25)
            pygame.draw.circle(screen, GRAY, center, 25)  

        elif self.shape == "cuttingboard":
            pygame.draw.rect(screen, WHITE, pygame.Rect(self.pos[0], self.pos[1], 50, 50))
            pygame.draw.line(screen, BLACK, (self.pos[0], self.pos[1] + 25), (self.pos[0] + 50, self.pos[1] + 25), 2) 
        
        elif self.shape == "onion":
            pygame.draw.rect(screen, ONION, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

        elif self.shape == "table":
            pygame.draw.rect(screen, WHITE, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

    def getState(self):
        return super().getState(self) + [self.pos,self.item]
    