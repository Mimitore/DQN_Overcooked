from Vegetable import Vegetable
from Cookware import Cookware

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

    @staticmethod
    def process_interaction(item,obj):
        if isinstance(item, Vegetable) and item.isCut:
            if isinstance(obj, Cookware):
                print('c\'est dans la marmite')
                obj.add_ingredient(item)
                item.crate.removeItem(item)
        

    def cooking(pot):
        if pot.ingredients != [] and pot.isOnStove:  
            pot.isWarm = True
            print("Le pot a cuit miam :)")
        else:
            print("Le pot n'a pas cuit triste :(")