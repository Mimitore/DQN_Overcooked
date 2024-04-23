from Container import Container
from HotStove import HotStove

class Cookware(Container):
    def __init__(self, pos, shape):
        super().__init__(pos, shape)
        self.isWarm = False
    
    def isOnStove(self, player):
        for obj in player.interactables:
            if isinstance(obj, HotStove):
                if obj.pos == self.pos:
                    return True
        return False

    def draw(self, screen):
            super().draw(screen) 

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    
    def interact(self, player):
        return super().interact(player)
    
    def draw(self, screen):
        return super().draw(screen)
    
    def add_ingredient(self, item):
        return super().add_ingredient(item)
    
    