import pygame # type: ignore
import sys
from CookingStation import CookingStation
from HotStove import HotStove
from CuttingBoard import CuttingBoard
from FoodCrate import FoodCrate
from Player import Player
from Item import Item
from Vegetable import Vegetable
from Container import Container
from Cookware import Cookware
from InteractionManager import InteractionManager
from config import BLACK,WHITE,ONION,GRAY

pygame.init()

# Taille de la fenêtre
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Overcooked')

clock = pygame.time.Clock()

# Positions initiales 
player = Player(50,50)


# Création des objets 
stove = HotStove((0, 0))
cuttingboard = CuttingBoard((450,450))
onioncrate = FoodCrate((0,450),"onion")
pot = Cookware((0,0),"pot")

player.interactables = [onioncrate, cuttingboard, stove, pot]

# Définition des collisions 
obstacles = [
    pygame.Rect(0, 0, 50,50),
    pygame.Rect(0,450,50,50),
    pygame.Rect(450,450,50,50)
]


def check_collision(player_rect, obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Gestion des touches
    keys = pygame.key.get_pressed()
    player.update_position(keys, obstacles)

    if keys[pygame.K_SPACE]:
        if player.held_item:
                # Poser le pot sur la cuisinière
                if player.is_facing(stove):
                    InteractionManager.cooking(pot)
                    
                # Poser un vegetable sur la cuttingboard
                if isinstance(player.held_item, Vegetable) and player.is_facing(cuttingboard):
                    cuttingboard.place_item(player.held_item)
                    print(f"Le joueur a posé un {player.held_item} sur la cuttingboard")
                
                # Si le joueur tient un objet et appuie sur espace, relâcher cet objet
                player.drop_item()
        else:
            # Sinon, interagir avec les objets environnants pour en prendre un
            player.interact()

    if keys[pygame.K_c]:
        if player.is_facing(cuttingboard):
            cuttingboard.cut_item()

    # Interface graphique
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player.rect) #player

    stove.draw(screen)
    cuttingboard.draw(screen)
    onioncrate.draw(screen)
    pot.draw(screen)

    # MàJ
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
sys.exit()