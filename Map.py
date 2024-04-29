import pygame
from Vegetable import Vegetable
from Container import Container
from ObjectsID import ObjectsID
class Map:
    def __init__(self,player,score):
        self.objects = []  # Liste pour stocker tous les objets interactables
        self.obstacles = []  # Liste pour gérer les obstacles
        self.player = player
        self.score = score

    def add_object(self, obj):
        if isinstance(obj, pygame.Rect):  # Si c'est un obstacle
            self.obstacles.append(obj)
        else:
            obj_type_id = getattr(obj, 'type_id', None)

            # Les obj à resteindre
            restricted_types = [ObjectsID.ONION, ObjectsID.PLATE]

            # Vérifier si l'objet appartient à un type restreint et peut être ajouté
            if obj_type_id in restricted_types:
                if isAddable(obj, self.objects, obj_type_id):
                    self.objects.append(obj)
                else:
                    print(f"There's too many of {obj_type_id} already.")
            else:
                # Si l'objet n'est pas de type restreint, l'ajouter sans vérification
                self.objects.append(obj)

    def remove_object(self,obj):
        self.objects.remove(obj)

    def draw(self, screen):
        self.player.draw(screen)
        self.score.draw(screen)
        for obj in self.objects:
            if hasattr(obj, 'draw'):
                obj.draw(screen)  # Appelle la méthode draw de chaque objet si elle existe
        

    def check_collisions(self, player_rect):
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False
    
def isAddable(obj,obj_list, target_type_id):
    """
    Verifie si tel obj peut etre ajouté dans le jeu ou non. Un tel obj de tel classe doit pas depasser au delà de 5
    """

    count = sum(1 for o in obj_list if getattr(o, 'type_id', None) == target_type_id)
    return getattr(obj, 'type_id', None) == target_type_id and count < 5