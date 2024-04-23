from Container import Container

class Cookware(Container):
    def __init__(self, pos, shape):
        super().__init__(pos, shape)
        self.state = "no-heat"

    def cooking(self):
        if self.ingredients != []:  
            self.state = "heat"
            print("Le pot a cuit miam :)")
        else:
            print("Le pot n'a pas cuit triste :(")

    def draw(self, screen):
            super().draw(screen) 

    def update_position(self, player_x, player_y):
        return super().update_position(player_x, player_y)
    
    def interact(self, player):
        return super().interact(player)
    
    def draw(self, screen):
        return super().draw(screen)
    
    