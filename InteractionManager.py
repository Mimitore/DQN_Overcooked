from Vegetable import Vegetable
from Cookware import Cookware
from Item import Item
from CookingStation import CookingStation

class InteractionManager:

    @staticmethod
    def calculate_offset(direction):
        offsets = {
            'left': (-50, 0),
            'right': (50, 0),
            'up': (0, -50),
            'down': (0, 50)
        }
        return offsets.get(direction, (0, 0))


    def process_interaction(self,item, obj):
        if isinstance(item, Vegetable) and isinstance(obj, Cookware):
            if item.isCut:  
                print('c\'est dans la marmite')
                obj.add_ingredient(item)
                return "del"
            else:
                print("Le légume n'est pas coupé.")
                return "keep"

        elif isinstance(item, Item) and isinstance(obj,CookingStation): 
            if obj.is_blocked:
                print("Non, c'est bloqué D:<")
                return "keep"
            else:
                return 'drop'
        return "drop"
            

    def cooking(pot):
        if pot.ingredients != [] and pot.isOnStove:  
            pot.isWarm = True
            print("Le pot a cuit miam :)")
        else:
            print("Le pot n'a pas cuit triste :(")