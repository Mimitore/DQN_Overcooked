from CookingStation import CookingStation
from Vegetable import Vegetable
from ObjectsID import ObjectsID

class FoodCrate(CookingStation):
    def __init__(self,pos,shape):
        super().__init__(pos, shape, ObjectsID.FOOD_CRATE_ONION)
        self.item_type = "onion"


    def draw(self, screen):
            super().draw(screen) 


    def checkBlocked(self, map):
        return super().checkBlocked(map)


    def interact(self, map):
        super().interact(map)
        
        if map.player.is_facing(self):
            if not self.is_blocked: # Si la caisse n'a pas d'objet sur lui qui le bloque
                if map.player.held_item is None:
                    new_item = Vegetable(self.pos,self.item_type,self)
                    map.player.take_item(new_item)
                    map.add_object(new_item)
                    print(f"Le joueur a pris un {new_item} de la caisse.")
                else:
                    print(f"Le joueur tient déjà un {map.player.held_item}.")
            
            else:
                print("Un objet bloque la caisse, impossible de prendre un item.")
         
    def get_state(self):
        return super().get_state(self)