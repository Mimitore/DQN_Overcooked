from CookingStation import CookingStation

class HotStove(CookingStation):
    def __init__(self,pos):
        
        super().__init__(pos,"hotstove")


    def draw(self, screen):
            super().draw(screen) 