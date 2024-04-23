from Container import Container

class Cookware(Container):
    def __init__(self, pos, shape):
        super().__init__(pos, shape)


    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    
    def interact(self, player):
        return super().interact(player)
    
    def draw(self, screen):
        return super().draw(screen)
    
    