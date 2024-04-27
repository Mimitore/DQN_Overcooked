from CookingStation import CookingStation
from ObjectsID import ObjectsID

class HotStove(CookingStation):
    def __init__(self,pos):
        
        super().__init__(pos,"hotstove",ObjectsID.HOT_STOVE)


    def draw(self, screen):
            super().draw(screen) 

    def getState(self):
        return super().getState(self)