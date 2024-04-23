from Vegetable import Vegetable
from Cookware import Cookware

class InteractionManager:

    def handle_drop(self, player, direction):
        offset = self.calculate_offset(direction)
        new_pos = (player.rect[0] + offset[0], player.rect[1] + offset[1])
        player.held_item.setPos(new_pos)
        self.process_interaction(player.held_item)

    @staticmethod
    def calculate_offset(direction):
        offsets = {
            'left': (-50, 0),
            'right': (50, 0),
            'up': (0, -50),
            'down': (0, 50)
        }
        return offsets.get(direction, (0, 0))

    def process_interaction(self, item):
        if isinstance(item, Vegetable) and item.isCut:
            for obj in item.crate.interactables:
                if isinstance(obj, Cookware) and obj.pos == item.pos:
                    print('c\'est dans la marmite')
                    obj.add_ingredient(item)
                    item.crate.removeItem(item)