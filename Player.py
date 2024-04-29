import pygame
from Vegetable import Vegetable
from CuttingBoard import CuttingBoard
from config import WHITE
from Actions import Actions
from GameObject import GameObject
from ObjectsID import ObjectsID

class Player(GameObject):
    def __init__(self, initial_position,type_id = ObjectsID.PLAYER):
        super().__init__(type_id)
        self.initial_position = initial_position
        self.pos = list(initial_position) 
        self.held_item = None
        self.direction = "down"
        self.last_interact_time = None

    def getPos(self):
        return (self.pos[0],self.pos[1])
    
    def setPos(self,x,y):
        self.pos[0]= x
        self.pos[1] = y

    def setDirection(self, new_direction):
        self.direction = new_direction

    def is_facing(self, obj):
        tolerance = 10
        """ Vérifie si le joueur fait face à l'objet en se basant sur leur position relative et la direction du joueur. """
        dx = obj.pos[0] - self.pos[0]
        dy = obj.pos[1] - self.pos[1]
        if self.direction == "right" and dx >= 0 and abs(dy) < tolerance and abs(dx) <= 50:
            return True
        elif self.direction == "left" and dx <= 0 and abs(dy) < tolerance and abs(dx) <= 50:
            return True
        elif self.direction == "up" and dy <= 0 and abs(dx) < tolerance and abs(dy) <= 50:
            return True
        elif self.direction == "down" and dy >= 0 and abs(dx) < tolerance and abs(dy) <= 50:
            return True
        return False
    
    def move(self, dx, dy, obstacles):
        # Copie temporaire pour tester le déplacement
        
        temp_rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50).copy()
        temp_rect.x += dx
        temp_rect.y += dy
        
        # Vérifier les limites de l'écran et les obstacles
        if temp_rect.x >= 0 and temp_rect.x <= 450 and temp_rect.y >= 0 and temp_rect.y <= 450:
            if not any(temp_rect.colliderect(ob) for ob in obstacles):
                self.pos = temp_rect[0],temp_rect[1]
        self.update_item_position()


    def execute_human_actions(self, keys, game_map):
        # Gestion des mouvements
        player_speed = 50
        if keys[pygame.K_LEFT]:
            self.move(-player_speed, 0, game_map.obstacles)
            self.setDirection("left")
        elif keys[pygame.K_RIGHT]:
            self.move(player_speed, 0, game_map.obstacles)
            self.setDirection("right")
        elif keys[pygame.K_UP]:
            self.move(0, -player_speed, game_map.obstacles)
            self.setDirection("up")
        elif keys[pygame.K_DOWN]:
            self.move(0, player_speed, game_map.obstacles)
            self.setDirection("down")

        # Gestion des interactions
        if keys[pygame.K_SPACE]:
            self.update_item_position()
            if self.held_item:
                # Relâcher un objet
                self.drop_item(game_map)
            else:
                # Interagir avec l'environnement
                self.interact(game_map)

        # Gestion de la découpe
        if keys[pygame.K_c]:
            self.cut(game_map)

    def execute_actions(self, action, game_map):
        result = ''
        player_speed = 50

        # Mouvement
        if action == Actions.LEFT:
            self.move(-player_speed, 0, game_map.obstacles)
            self.setDirection("left")
            return 'move'
        elif action == Actions.RIGHT:
            self.move(player_speed, 0, game_map.obstacles)
            self.setDirection("right")
            return 'move'
        elif action == Actions.UP:
            self.move(0, -player_speed, game_map.obstacles)
            self.setDirection("up")
            return 'move'
        elif action == Actions.DOWN:
            self.move(0, player_speed, game_map.obstacles)
            self.setDirection("down")
            return 'move'

        # Interactions
        elif action == Actions.SPACE:
            self.update_item_position()
            if self.held_item:
                result = self.drop_item(game_map)
            else:
                self.interact(game_map)

        # Découpe
        elif action == Actions.CUT:
            if (self.cut(game_map)):
                result = 'cut'

        return result 

    def interact(self,map):
        for obj in map.objects:
                obj.interact(map)

    def take_item(self, item):
        """ Le joueur prend un item s'il n'en tient pas déjà un. """
        if self.held_item is None and self.is_facing(item):
            self.held_item = item
            print(f"Le joueur prend un {item}.")
            self.update_item_position()
            print(item.pos)
        else:
            print(f"Le joueur tient déjà un {self.held_item}.")


    def update_item_position(self):
        if self.held_item:
            self.held_item.update_position(self.pos[0], self.pos[1])

    def drop_item(self,map):
        from InteractionManager import InteractionManager
        
        result = ''

        if self.held_item!=None:
            if(self.direction):
                offset = InteractionManager().calculate_offset(self.direction)

            new_pos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
            status = self.held_item.isDropable(new_pos,map)

            if status == "drop":
                self.held_item.pos = new_pos
                print(f"Le joueur lâche un {self.held_item}.")
                self.held_item = None
                
            elif status == "del" or status == "tocookware" or status == "serv":
                self.held_item = None

                if status == 'tocookware' or status == 'serv':
                    result = status

            else:
                if status == 'toplate':
                    result = status
                print('keep ur object')

        return result

    def cut(self,map):
        if self.held_item == None:
            for obj in map.objects:
                if isinstance(obj, CuttingBoard) and self.is_facing(obj) and isinstance(obj.item,Vegetable):
                    obj.item.cut()
                    print("the vegetable is cut")
                    return True
        return False


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.pos[0], self.pos[1], 50, 50))

    def getState(self):
        return super().getState(self)+[self.pos,self.held_item]

    def reset(self):
        self.pos = list(self.initial_position)
        self.direction = "down"
        self.held_item = None
    
