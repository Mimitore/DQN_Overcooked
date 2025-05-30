from Vegetable import Vegetable
from Cookware import Cookware
from Item import Item
from CookingStation import CookingStation
from CuttingBoard import CuttingBoard
from Container import Container
from ServiceStation import ServiceStation

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
    def process_interaction(item, obj,map):
        if isinstance(item, Vegetable) and isinstance(obj, Cookware):
            if item.isCut and not obj.isFull():  
                print('c\'est dans la marmite')
                obj.add_ingredient(item)
                obj.cooking(map)
                map.remove_object(item)
                return "del"
            else:
                print("Le légume n'est pas coupé ou bien la marmite est remplie.")
                return 'nonvaliditem'#"keep"
        
        elif isinstance(item,Item) and isinstance(obj, CuttingBoard):
            obj.item = item
            return 'drop'
        
        elif isinstance(item,Item) and isinstance(obj, ServiceStation):
            # Verification si c'est un plat à servir sur le comptoir
            if isinstance(item,Container) and not isinstance(item,Cookware):
                if obj.checkPlate(item):
                    print('Un service est fait')
                    map.remove_object(item)
                    map.score.update_score()
                    return "serv"#"del"
                else:
                    print('plat non valide')
                    return "nonvaliditem"#"keep"
            else:
                print('plat non valide')
                return "nonvaliditem" #"keep"

        elif isinstance(item,Cookware) and isinstance(obj, Container):
            # A modifier plus tard lorsqu'on aura un autre type de soupe à faire
            if item.isFull() and obj.isEmpty() and obj.shape =="plate":
                item.transfer_ingredients_to(obj)
                obj.isFull()
                print("la soupe est dans l'assiette")
                return "toplate"#"keep"

        elif isinstance(item, Item) and isinstance(obj,CookingStation): 
            obj.checkBlocked(map)

            if obj.is_blocked:
                print("Non, c'est bloqué D:<")
                return "keep"
            else:
                return 'drop'
        return "drop"
            

