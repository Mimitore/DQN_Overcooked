import pygame

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