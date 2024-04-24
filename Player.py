import pygame
from Vegetable import Vegetable
from CuttingBoard import CuttingBoard


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.held_item = None
        self.direction = "down"
        self.last_interact_time = None
        self.interactables = []

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def setPos(self,x,y):
        self.rect[0]= x
        self.rect[1] = y


    def setDirection(self, new_direction):
        self.direction = new_direction

    def is_facing(self, obj):
        tolerance = 10
        """ Vérifie si le joueur fait face à l'objet en se basant sur leur position relative et la direction du joueur. """
        dx = obj.pos[0] - self.rect[0]
        dy = obj.pos[1] - self.rect[1]
        if self.direction == "right" and dx >= 0 and abs(dy) < tolerance and abs(dx) <= 50:
            return True
        elif self.direction == "left" and dx <= 0 and abs(dy) < tolerance and abs(dx) <= 50:
            return True
        elif self.direction == "up" and dy <= 0 and abs(dx) < tolerance and abs(dy) <= 50:
            return True
        elif self.direction == "down" and dy >= 0 and abs(dx) < tolerance and abs(dy) <= 50:
            return True
        return False

    def check_collision(player_rect, obstacles):
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False
    
    def move(self, dx, dy, obstacles):
        # Copie temporaire pour tester le déplacement
        
        temp_rect = self.rect.copy()
        temp_rect.x += dx
        temp_rect.y += dy
        
        # Vérifier les limites de l'écran et les obstacles
        if temp_rect.x >= 0 and temp_rect.x <= 450 and temp_rect.y >= 0 and temp_rect.y <= 450:
            if not any(temp_rect.colliderect(ob) for ob in obstacles):
                self.rect = temp_rect
        self.update_item_position()

    def update_position(self, keys, obstacles):
        player_speed = 50
        if keys[pygame.K_LEFT]:
            self.move(-player_speed, 0, obstacles)
            self.setDirection("left")
        if keys[pygame.K_RIGHT]:
            self.move(player_speed, 0, obstacles)
            self.setDirection("right")
        if keys[pygame.K_UP]:
            self.move(0, -player_speed, obstacles)
            self.setDirection("up")
        if keys[pygame.K_DOWN]:
            self.move(0, player_speed, obstacles)
            self.setDirection("down")

    def interact(self):
        for obj in self.interactables:
            obj.interact(self)

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
            self.held_item.update_position(self.rect[0], self.rect[1])

    def drop_item(self):
        from InteractionManager import InteractionManager
        if self.held_item!=None:
            
            if(self.direction):
                offset = InteractionManager().calculate_offset(self.direction)

            new_pos = (self.rect[0] + offset[0], self.rect[1] + offset[1])

            
            status = self.held_item.isDropable(new_pos,self.interactables)

            if status == "drop":
                self.held_item.pos = new_pos
                print(f"Le joueur lâche un {self.held_item}.")
                self.held_item = None
            elif status == "del":
                self.held_item.crate.removeItem(self.held_item)
                self.held_item = None

            else:
                print('keep ur object')

    def cut(self):
        if self.held_item == None:
            for obj in self.interactables:
                if isinstance(obj, CuttingBoard) and self.is_facing(obj) and isinstance(obj.item,Vegetable):
                    obj.item.cut()
                    print("the vegetable is cut")
                    break
                