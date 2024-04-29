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
        self.restricted_types = [ObjectsID.ONION, ObjectsID.PLATE]



    def isAddable(self,obj,obj_list, target_type_id):
        """
        Verifie si tel obj peut etre ajouté dans le jeu ou non. Un tel obj de tel classe doit pas depasser au delà de 5
        """

        count = sum(1 for o in obj_list if getattr(o, 'type_id', None) == target_type_id)
        return getattr(obj, 'type_id', None) == target_type_id and count < 5
    
    def add_object(self, obj):
        if isinstance(obj, pygame.Rect):  # Si c'est un obstacle
            self.obstacles.append(obj)
        else:
            obj_type_id = getattr(obj, 'type_id', None)

            # Les obj à resteindre

            # Vérifier si l'objet appartient à un type restreint et peut être ajouté
            if obj_type_id in self.restricted_types:
                if self.isAddable(obj, self.objects, obj_type_id):
                    self.objects.append(obj)
                # else:
                #     print(f"There's too many of {obj_type_id} already.")
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
    
    def getState(self):
        state = []
        for obj in self.objects:
            state.extend(obj.getState()) 

        return state
    
    def getState(self):
        #Etat du joueur
        state = self.player.getState()


        # Préparer les listes pour chaque type d'objet avec des espaces fixes
        max_items = 5
        onions = [None] * max_items
        plates = [None] * max_items
        
        # Remplir les listes avec l'état des objets existants
        onion_count = 0
        plate_count = 0

        for obj in self.objects:
            obj_type_id = getattr(obj, 'type_id', None)
            if obj_type_id in self.restricted_types:
                if obj.type_id == ObjectsID.ONION and onion_count < max_items:
                    onions[onion_count] = obj.getState()
                    onion_count += 1
                elif obj.type_id == ObjectsID.PLATE and plate_count < max_items:
                    plates[plate_count] = obj.getState()
                    plate_count += 1
            else:
                state.extend(obj.getState())
        # Remplacement des None par une représentation par défaut pour les emplacements vides
        default_onion_state = [0, 0, 0,0]  # Chaque onion a 3 caractéristiques
        default_plate_state = [0, 0, 0,0]  # Chaque plate a 3 caractéristiques

        # Mise à jour des listes onions et plates pour remplacer les None par les valeurs par défaut
        onions = [onion_state if onion_state is not None else default_onion_state for onion_state in onions]
        plates = [plate_state if plate_state is not None else default_plate_state for plate_state in plates]

        # Étendre state avec les éléments individuels des listes onions et plates
        for onion_state in onions:
            state.extend(onion_state)  # Étend chaque élément individuellement au lieu de sous-listes

        for plate_state in plates:
            state.extend(plate_state)  # De même pour les plates

        clean_state = [0 if x is None else x for x in state]
        return clean_state



    def reset(self):
        self.objects = []
        self.obstacles = []

        self.score.reset() 
        self.player.reset()  

