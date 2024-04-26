from CookingStation import CookingStation
from Player import Player
from Vegetable import Vegetable

class FoodCrate(CookingStation):
    def __init__(self,pos,shape):
        super().__init__(pos,shape)
        self.item_type = "onion"
        self.items = []


    def draw(self, screen):
            super().draw(screen) 
            # for item in self.items:
            #     item.draw(screen)

    def checkBlocked(self, map):
        return super().checkBlocked(map)
    
    def removeItem(self,item):
        if item in self.items:
            print("item removed")
            self.items.remove(item)
            print(self.items)

    def interact(self, map):
        super().interact(map)
        
        if map.player.is_facing(self):
            if not self.is_blocked: # Si la caisse n'a pas d'objet sur lui qui le bloque
                if map.player.held_item is None:
                    new_item = Vegetable(self.pos,self.item_type,self)
                    map.player.take_item(new_item)
                    self.items.append(new_item)
                    map.objects.append(new_item)
                    print(f"Le joueur a pris un {new_item} de la caisse.")
                else:
                    print(f"Le joueur tient déjà un {map.player.held_item}.")
            
            else:
                print("Un objet bloque la caisse, impossible de prendre un item.")
         
