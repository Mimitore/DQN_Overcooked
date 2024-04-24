from Vegetable import Vegetable
from Cookware import Cookware
from Item import Item
from CookingStation import CookingStation
from CuttingBoard import CuttingBoard

class InteractionManager:

    def __init__(self):
        self.interactables = []
        
    @staticmethod
    def calculate_offset(direction):
        offsets = {
            'left': (-50, 0),
            'right': (50, 0),
            'up': (0, -50),
            'down': (0, 50)
        }
        return offsets.get(direction, (0, 0))


    def process_interaction(self,item, obj,interactables):
        if isinstance(item, Vegetable) and isinstance(obj, Cookware):
            if item.isCut and not obj.isFull():  
                print('c\'est dans la marmite')
                obj.add_ingredient(item)
                obj.cooking(interactables)
                return "del"
            else:
                print("Le légume n'est pas coupé ou bien la marmite est remplie.")
                return "keep"


        elif isinstance(item, Item) and isinstance(obj,CookingStation): 
            obj.checkBlocked(interactables)

            if obj.is_blocked:
                print("Non, c'est bloqué D:<")
                return "keep"
            else:
                return 'drop'
        return "drop"
            

