from CookingStation import CookingStation
from Player import Player
from Item import Item
class FoodCrate(CookingStation):
    def __init__(self,pos,shape):
        super().__init__(pos,shape)
        self.item_type = "onion"
        self.items = []


    def draw(self, screen):
            super().draw(screen) 
            for item in self.items:
                item.draw(screen)

    def checkBlocked(self, player):
        return super().checkBlocked(player)
    

    def interact(self, player):
        super().interact(player)
        if player.is_facing(self):
            if not self.is_blocked:
                if player.held_item is None:
                    new_item = Item(self.pos,self.item_type)
                    player.take_item(new_item)
                    self.items.append(new_item)
                    player.interactables.append(new_item)
                    print(f"Le joueur a pris un {new_item} de la caisse.")
                else:
                    print(f"Le joueur tient déjà un {player.held_item}.")
            
            else:
                print("Un objet bloque la caisse, impossible de prendre un item.")
         
